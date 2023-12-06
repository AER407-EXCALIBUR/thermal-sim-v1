from base_classes import ThermalComponent, Heater

# Initial temperature does not matter for these
# Illumination factor also does not matter so much


def get_components(case_flags: dict) -> list[ThermalComponent]:
    """
    Returns spacecraft components based on case flags

    Parameters
    ----------
    case_flags: dict
        dictionary of case flags


    Returns
    -------
    list[ThermalComponent]
        list of spacecraft components
    """

    """
    Radiators
    - 3.1 x 6.5 m rectangle facing into space always
    - Aluminum radiator, assuming it's a 1 mm thick sheet, which only radiates on one side
    """
    RADIATORS = ThermalComponent(
        mass=50,
        shc=890,
        rad_area=20 if case_flags["radiators"] else 0,
        emissivity=0.95,
        temp=293,
        illumination_factor=0,
        innate_power=100 if case_flags["rhus"] else 0,
        heater=Heater(power=0, set_temp=0),
    )

    """
    Structure
    - 400 kg aluminum structure, mostly insulated from the environment
    - Assume it's just the main tube of the spacecraft
    - 2.5 m diam cylinder x 4.5 m height = 25m^2 of radiative area
    - Insulation alteras emissivity roughly by a factor of 1/n, where n is the number of layers
    - Assume 40 layers of MLI
    - Assume 33% illumination by the Sun
    """
    STRUCTURE = ThermalComponent(
        mass=400,
        shc=890,
        rad_area=25,
        emissivity=0.95 / 40
        if case_flags["insulation"]
        else (0.3 if case_flags["paint"] else 0.95),
        temp=293,
        illumination_factor=0.33,
        innate_power=100 if case_flags["rhus"] else 0,
        heater=Heater(power=20, set_temp=220),
    )

    """
    Electronics
    - GNC
    - TCO electronics
    - CDH
    - Batteries
    - Completely internal, shielded from radiation
    - Computers generated a combined power of 400 W continuously
    """
    ELECTRONICS = ThermalComponent(
        mass=100,
        shc=890,
        rad_area=0,
        emissivity=0,
        temp=293,
        illumination_factor=0,
        innate_power=400
        if case_flags["electronics_active"]
        else (100 if case_flags["rhus"] else 0),
        heater=Heater(power=100, set_temp=293),
    )

    """
    Solar Arrays
    - 230 m^2 sun collection area, means the other side (230 m^2 also) is radiating away heat
    - solar arrays are 30% efficient, so the effective illuminated area is 0.5 * 0.7 = 0.35
    """
    SOLAR_ARRAYS = ThermalComponent(
        mass=1000,
        shc=890,
        rad_area=230 * 2,
        emissivity=0.8,
        temp=293,
        illumination_factor=0.35,
        innate_power=100 if case_flags["rhus"] else 0,
        heater=Heater(power=100, set_temp=293),
    )

    """
    Sample Box
    - 20 kg highly insulated box, connected to radiators via 40 W heat pump, and weakly to the structure
    - minimal amount of radiative area, around 5 m^2
    - emissivity is 0.01 by virtue of nearly 100 layers of MLI>?
    - 50% illuminated by the Sun
    - 10 W intrinstic power draw?
    """
    SAMPLE_BOX = ThermalComponent(
        mass=20,
        shc=890,
        rad_area=5,
        emissivity=0.01,
        temp=180,
        illumination_factor=0.5,
        innate_power=10 if case_flags["electronics_active"] else 0,
        heater=Heater(power=0, set_temp=0),
    )

    """
    Propellant Tanks
    - 5000 kg of propellant
    - Tank heaters to heat up propellants to room temp
    """
    PROP_TANKS = ThermalComponent(
        mass=5000,
        shc=500,
        rad_area=0,
        emissivity=0,
        temp=293,
        illumination_factor=0,
        innate_power=100 if case_flags["rhus"] else 0,
        heater=Heater(power=100, set_temp=293),
    )

    """
    Engines
    - about 50 kg
    - engine innate power can range from 0 to thousands of W, but let's assume 0
    """
    ENGINES = ThermalComponent(
        mass=50,
        shc=890,
        rad_area=1,
        emissivity=0.95,
        temp=293,
        illumination_factor=0.3,
        innate_power=0,
        heater=Heater(power=0, set_temp=0),
    )

    """
    Antenna
    - about 30 kg
    - insulated using MLI (let's say 20 layers)
    - 3m diameter dish, taken to be surface area
    - integrated heater which tries to keep the temperature at 293 K
    - faces opposite the radiator, so it's in almost full sunlight
    """
    ANTENNA = ThermalComponent(
        mass=30,
        shc=890,
        rad_area=3**2 / 4 * 3.14,
        emissivity=0.95 / 20,
        temp=293,
        illumination_factor=0.7,
        innate_power=30,
        heater=Heater(power=20, set_temp=293),
    )

    return [
        RADIATORS,
        STRUCTURE,
        ELECTRONICS,
        SOLAR_ARRAYS,
        SAMPLE_BOX,
        PROP_TANKS,
        ENGINES,
        ANTENNA,
    ]
