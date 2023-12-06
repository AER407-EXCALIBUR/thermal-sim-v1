from multiprocessing import Pool

from matplotlib import pyplot as plt
from scipy.integrate import solve_ivp

from base_classes import EnvironmentalConditions, ThermalArchitecture
from environmental_prefabs import EARTH, ENCELADUS, VENUS
from odes import thermal_ode
from spacecraft_prefabs import get_srs
from functools import partial

from case_flags import (
    NOMINAL_CASES,
    INSULATION_PAINT_TRADE_CASES,
    HEATER_RHU_TRADE_CASES,
    RADIATOR_LOUVER_TRADE_CASES,
    ACTIVE_COOLING_TRADE_CASES,
)


def run_sim(
    spacecraft: ThermalArchitecture,
    case_flags: dict,
    case_name: str,
    environment: EnvironmentalConditions,
    show: bool = False,
):
    """
    Runs a simulation of the thermal architecture
    """
    sol = solve_ivp(
        thermal_ode,
        (0, 1e6),
        list(spacecraft.to_state()) + [0, 0, 0, 0],
        args=(spacecraft, environment, case_flags),
        method="RK45",
        atol=1e-2,
    )

    # Plot
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.plot(sol.t, sol.y[0, :], label="Radiators")
    ax.plot(sol.t, sol.y[1, :], label="Structure")
    ax.plot(sol.t, sol.y[2, :], label="Electronics")
    ax.plot(sol.t, sol.y[3, :], label="Solar Arrays")
    ax.plot(sol.t, sol.y[4, :], label="Sample Box")
    ax.plot(sol.t, sol.y[5, :], label="Propellant Tanks")
    ax.plot(sol.t, sol.y[6, :], label="Engines")
    ax.plot(sol.t, sol.y[7, :], label="Antenna")
    ax.legend()
    ax.set_ylabel("Component Temperature (K)")
    ax.set_xlabel("Time (s)")
    ax.grid()
    ax.set_title(f"Thermal Sim - {environment.name}\n" + case_name)

    fig.savefig(f"outputs/{environment.name}_case_{case_name}.png", dpi=300)
    with open(f"outputs/{environment.name}_case_{case_name}.txt", "w") as f:
        f.write(str(case_flags) + "\n\n")

        labels = [
            "Avg Innate Power Draw",
            "Avg Heater Power Draw",
            "Avg Incoming Radiative Power",
            "Avg Rejected Radiative Power",
        ]

        for idx, label in enumerate(labels):
            num_components = len(spacecraft.components)

            power_value = (
                sol.y[num_components + idx, -1] - sol.y[num_components + idx, -2]
            ) / (sol.t[-1] - sol.t[-2])
            f.write(f"{label}: {power_value:.2f} W\n")

    if show:
        plt.show()


if __name__ == "__main__":
    cases = {
        "Nominal": NOMINAL_CASES,
        "Insulation/Paint Trade": INSULATION_PAINT_TRADE_CASES,
        "Heater/RHU Trade": HEATER_RHU_TRADE_CASES,
        "Radiator/Louver Trade": RADIATOR_LOUVER_TRADE_CASES,
        "Active Cooling Trade": ACTIVE_COOLING_TRADE_CASES,
    }

    sim_type = "Nominal"

    case_flag_collection = cases[sim_type]

    case_flag_collection = (
        NOMINAL_CASES
        | INSULATION_PAINT_TRADE_CASES
        | HEATER_RHU_TRADE_CASES
        | RADIATOR_LOUVER_TRADE_CASES
        | ACTIVE_COOLING_TRADE_CASES
    )

    environments = [ENCELADUS, VENUS, EARTH]
    spacecraft_architectures = [
        get_srs(case_flags) for case_flags in case_flag_collection.values()
    ]

    s = ""
    i = 0

    for environment in environments:
        print(f"Simulating {environment}")

        for spacecraft, case_flags, case_name in zip(
            spacecraft_architectures,
            case_flag_collection.values(),
            case_flag_collection.keys(),
        ):
            i += 1
            s += (
                r"\newpage \textbf{"
                + f"Thermal Sim - {environment.name} - {case_name}"
                + r"}"
                + "\n\n"
            )
            s += (
                r"""
    \includegraphics[width=\textwidth]{"""
                + f"thermal_sim/{environment.name}_case_{case_name}.png"
                + r"""}
"""
            )

    with open("thermal_sim.tex", "w") as f:
        f.write(s)

    # with Pool() as pool:
    #     for environment in environments:
    #         print(f"Simulating {environment}")

    #         partial_run_sim = partial(run_sim, environment=environment, show=False)
    #         pool.starmap(
    #             partial_run_sim,
    #             zip(
    #                 spacecraft_architectures,
    #                 case_flag_collection.values(),
    #                 case_flag_collection.keys(),
    #             ),
    #         )
