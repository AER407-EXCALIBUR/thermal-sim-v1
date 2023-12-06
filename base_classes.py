from dataclasses import dataclass
import numpy.typing as npt
import numpy as np


@dataclass
class ThermalLink:
    conductance: float

    def get_conductance(self, self_temp, other_temp):
        """
        Gets conductance as a result of self temperature and other temperature
        """
        return self.conductance


@dataclass
class ThermalSwitch(ThermalLink):
    cool_limit: float
    heat_limit: float
    attenuation_factor: float

    def get_conductance(self, self_temp, other_temp):
        """
        Gets conductance as a result of self temperature and other temperature

        Shuts off thermal link (decreasing its conductance) when it's either too
        hot or too cold
        """
        if other_temp > self_temp and self_temp > self.heat_limit:
            return self.conductance / self.attenuation_factor

        elif other_temp < self_temp and self_temp < self.cool_limit:
            return self.conductance / self.attenuation_factor

        else:
            return self.conductance


@dataclass
class Heater:
    power: float  # W
    set_temp: float  # K, heater turns off above this temperature


@dataclass
class ThermalComponent:
    mass: float  # mass [kg]
    shc: float  # specific heat capacity [J/(kg*K)]
    rad_area: float  # radiative area [m^2]
    emissivity: float  # 0 to 1, emissivity

    temp: float  # temperature [K]
    illumination_factor: float  # 0 to 1; how much of the radiative area is lit by the Sun?
    innate_power: float  # intrinsic power generation factor, either from heaters or otherwise (W)

    heater: Heater  # electric heater used to keep the device warm

    @property
    def thermal_inertia(self) -> float:
        return self.mass * self.shc


@dataclass
class ThermalArchitecture:
    components: list[ThermalComponent]
    conductivity_matrix: npt.NDArray[np.floating]
    active_transport_matrix: npt.NDArray[np.floating]

    def to_state(self) -> npt.NDArray[np.floating]:
        # Turns the spacecraft thermal architecture into a state form
        # (just the temperatures)
        return np.array([component.temp for component in self.components])

    def update_from_state(self, temps: npt.NDArray[np.floating]):
        # Update state to spacecraft properties
        for idx, component in enumerate(self.components):
            component.temp = temps[idx]

    @property
    def component_thermal_inertias(self) -> npt.NDArray[np.floating]:
        return np.array([component.thermal_inertia for component in self.components])


@dataclass
class EnvironmentalConditions:
    name: str
    incident_radiative_flux: float  # W/m^2
    background_temp: float  # K, usually the temperature of space, 2.7 K
