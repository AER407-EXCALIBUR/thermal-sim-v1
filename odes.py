import numpy as np
from base_classes import ThermalArchitecture, EnvironmentalConditions

from heat_transfer import (
    incident_radiation_flux,
    background_radiation_flux,
    conduction_flux,
)


def thermal_ode(
    t: float,
    y: np.ndarray,
    spacecraft: ThermalArchitecture,
    environment: EnvironmentalConditions,
    case_flags: dict,
) -> np.ndarray:
    """
    Computes heat transfer between components of the spacecraft and the environment

    Parameters
    ----------
    t: float
        time (s)
    y: np.ndarray
        state vector, temperatures of the components in K
    spacecraft: ThermalArchitecture
        spacecraft thermal architecture
    environment: EnvironmentalConditions
        environmental conditions surrounding the spacecraft
    case_flags: dict
        dictionary of case flags

    Returns
    -------
    np.ndarray
        derivative of the state vector, temperatures of the components in K/s

    Math
    ----
    dT/dt = (Q_in - Q_out) / (thermal inertia)
    """
    num_components = len(spacecraft.components)

    # Update temperatures
    spacecraft.update_from_state(y[0:num_components])

    # Get temperatures from spacecraft
    temps = spacecraft.to_state()
    assert np.allclose(temps, y[0:num_components])

    fluxes = np.zeros_like(temps)
    yp = np.zeros_like(y)

    for i, component in enumerate(spacecraft.components):
        # 1A. Innate power
        fluxes[i] += component.innate_power
        yp[num_components] += component.innate_power

        if case_flags["electric_heaters"]:
            # 1B. Heater input
            if component.temp < component.heater.set_temp:
                fluxes[i] += component.heater.power
                yp[num_components + 1] += component.heater.power

        # 2A. Radiation flux
        incident_flux = incident_radiation_flux(component, environment)
        background_flux = background_radiation_flux(component, environment)

        # 2B. Louver attenuation
        louver_attenuation_factor = 10 if case_flags["louvers"] else 1

        # hot range based on heater set temp
        if component.temp > component.heater.set_temp and incident_flux > 0:
            incident_flux /= louver_attenuation_factor

        # arbitrary cold range
        # if component.temp < 193 and background_flux < 0:
        #     background_flux /= louver_attenuation_factor

        yp[num_components + 2] += incident_flux
        yp[num_components + 3] += background_flux
        fluxes[i] += incident_flux + background_flux

        # 3. Conduction flux
        for j, other_component in enumerate(spacecraft.components):
            fluxes[i] += conduction_flux(
                other_component, component, spacecraft.conductivity_matrix[i][j]
            )

            fluxes[i] += spacecraft.active_transport_matrix[i, j]

    # Divide fluxes by component inertia
    yp[0:num_components] = fluxes / spacecraft.component_thermal_inertias

    # power draw included in yp
    return yp
