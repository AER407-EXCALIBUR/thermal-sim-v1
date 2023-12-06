# Set case flags
FINAL_DESIGN_ELEC_OFF = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

FINAL_DESIGN_ELEC_ON = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": True,
    "louvers": True,
}

NOTHING = {
    "electric_heaters": False,
    "rhus": False,
    "radiators": False,
    "paint": False,
    "insulation": False,
    "active_cooling": False,
    "electronics_active": False,
    "louvers": False,
}

NOTHING_WITH_INSULATION = {
    "electric_heaters": False,
    "rhus": False,
    "radiators": False,
    "paint": False,
    "insulation": True,
    "active_cooling": False,
    "electronics_active": False,
    "louvers": False,
}

NOTHING_WITH_PAINT = {
    "electric_heaters": False,
    "rhus": False,
    "radiators": False,
    "paint": True,
    "insulation": False,
    "active_cooling": False,
    "electronics_active": False,
    "louvers": False,
}

INSULATION_AND_PAINT_BASELINE = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": True,
    "paint": False,
    "insulation": False,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

BASELINE_WITH_INSULATION = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

BASELINE_WITH_PAINT = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": True,
    "paint": True,
    "insulation": False,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

NOTHING_WITH_RADIATORS = {
    "electric_heaters": False,
    "rhus": False,
    "radiators": True,
    "paint": False,
    "insulation": False,
    "active_cooling": False,
    "electronics_active": False,
    "louvers": False,
}

NOTHING_WITH_RADIATORS_AND_LOUVERS = {
    "electric_heaters": False,
    "rhus": False,
    "radiators": True,
    "paint": False,
    "insulation": False,
    "active_cooling": False,
    "electronics_active": False,
    "louvers": True,
}

RADIATOR_LOUVER_BASELINE = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": False,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": False,
}

BASELINE_WITH_RADIATORS = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

BASELINE_WITH_RADIATORS_AND_LOUVERS = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

NOTHING_WITH_HEATERS = {
    "electric_heaters": True,
    "rhus": False,
    "radiators": False,
    "paint": False,
    "insulation": False,
    "active_cooling": False,
    "electronics_active": False,
    "louvers": False,
}

NOTHING_WITH_RHUS = {
    "electric_heaters": False,
    "rhus": True,
    "radiators": False,
    "paint": False,
    "insulation": False,
    "active_cooling": False,
    "electronics_active": False,
    "louvers": False,
}

NOTHING_WITH_HEATERS_AND_RHUS = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": False,
    "paint": False,
    "insulation": False,
    "active_cooling": False,
    "electronics_active": False,
    "louvers": False,
}

HEATER_RHU_BASELINE = {
    "electric_heaters": False,
    "rhus": False,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

BASELINE_WITH_HEATERS = {
    "electric_heaters": True,
    "rhus": False,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

BASELINE_WITH_RHUS = {
    "electric_heaters": False,
    "rhus": True,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

BASELINE_WITH_HEATERS_AND_RHUS = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

NOTHING_WITH_ACTIVE_COOLING = {
    "electric_heaters": False,
    "rhus": False,
    "radiators": False,
    "paint": False,
    "insulation": False,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

ACTIVE_COOLING_BASELINE = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": False,
    "electronics_active": False,
    "louvers": True,
}

BASELINE_WITH_ACTIVE_COOLING = {
    "electric_heaters": True,
    "rhus": True,
    "radiators": True,
    "paint": False,
    "insulation": True,
    "active_cooling": True,
    "electronics_active": False,
    "louvers": True,
}

######################################################################################

INSULATION_PAINT_TRADE_CASES = {
    "Nothing": NOTHING,
    "Nothing with insulation": NOTHING_WITH_INSULATION,
    "Nothing with paint": NOTHING_WITH_PAINT,
    "Insulation and paint baseline": INSULATION_AND_PAINT_BASELINE,
    "Baseline with insulation": BASELINE_WITH_INSULATION,
    "Baseline with paint": BASELINE_WITH_PAINT,
}

RADIATOR_LOUVER_TRADE_CASES = {
    "Nothing": NOTHING,
    "Nothing with radiators": NOTHING_WITH_RADIATORS,
    "Nothing with radiators and louvers": NOTHING_WITH_RADIATORS_AND_LOUVERS,
    "Radiator louver baseline": RADIATOR_LOUVER_BASELINE,
    "Baseline with radiators": BASELINE_WITH_RADIATORS,
    "Baseline with radiators and louvers": BASELINE_WITH_RADIATORS_AND_LOUVERS,
}

HEATER_RHU_TRADE_CASES = {
    "Nothing": NOTHING,
    "Nothing with heaters": NOTHING_WITH_HEATERS,
    "Nothing with RHUs": NOTHING_WITH_RHUS,
    "Nothing with heaters and RHUs": NOTHING_WITH_HEATERS_AND_RHUS,
    "Heater RHU baseline": HEATER_RHU_BASELINE,
    "Baseline with heaters": BASELINE_WITH_HEATERS,
    "Baseline with RHUs": BASELINE_WITH_RHUS,
    "Baseline with heaters and RHUs": BASELINE_WITH_HEATERS_AND_RHUS,
}

ACTIVE_COOLING_TRADE_CASES = {
    "Nothing": NOTHING,
    "Nothing with active cooling": NOTHING_WITH_ACTIVE_COOLING,
    "Active cooling baseline": ACTIVE_COOLING_BASELINE,
    "Baseline with active cooling": BASELINE_WITH_ACTIVE_COOLING,
}

NOMINAL_CASES = {
    "electronics off": FINAL_DESIGN_ELEC_OFF,
    "electronics on": FINAL_DESIGN_ELEC_ON,
}
