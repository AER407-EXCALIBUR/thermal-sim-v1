from base_classes import ThermalArchitecture, ThermalLink, ThermalSwitch
from component_prefabs import get_components

import numpy as np


conductivity_matrix = [[ThermalLink(conductance=0) for _ in range(8)] for _ in range(8)]

# Radiators <-> Structure
conductivity_matrix[0][1] = ThermalLink(conductance=20)

# Radiators <-> Sample Box
# Thermal switch which shuts off which shuts off when radiator would heat component to greather than 160 K
# (limit for sample preservation is 193 K)
conductivity_matrix[0][4] = ThermalSwitch(
    conductance=20, cool_limit=0, heat_limit=160, attenuation_factor=100
)

# Structure <-> Components
# Structure <-> Electronics
conductivity_matrix[1][2] = ThermalSwitch(
    conductance=20, cool_limit=280, heat_limit=310, attenuation_factor=100
)
# Structure <-> Solar Arrays
conductivity_matrix[1][3] = ThermalSwitch(
    conductance=30, cool_limit=250, heat_limit=350, attenuation_factor=100
)
# Structure <-> Sample Box: Keep the sample box cold
conductivity_matrix[1][4] = ThermalSwitch(
    conductance=20, cool_limit=0, heat_limit=150, attenuation_factor=100
)
# Structure <-> Propellant Tanks: Keep hydrazine liquid
conductivity_matrix[1][5] = ThermalSwitch(
    conductance=10, cool_limit=288, heat_limit=400, attenuation_factor=100
)
# Structure <-> Engines
conductivity_matrix[1][6] = ThermalSwitch(
    conductance=10, cool_limit=250, heat_limit=300, attenuation_factor=100
)
# Structure <-> Antenna
conductivity_matrix[1][7] = ThermalSwitch(
    conductance=20, cool_limit=250, heat_limit=330, attenuation_factor=100
)

# Symmetrize Matrix
for i in range(int(len(conductivity_matrix) / 2)):
    for j in range(len(conductivity_matrix)):
        conductivity_matrix[j][i] = conductivity_matrix[i][j]


def get_srs(case_flags: dict) -> ThermalArchitecture:
    """
    Returns the sample return spacecraft thermal architecture
    for a given set of case flags

    Parameters
    ----------
    case_flags: dict
        dictionary of case flags


    Returns
    -------
    ThermalArchitecture
        the spacecraft thermal architecture
    """

    return ThermalArchitecture(
        get_components(case_flags),
        # Symmetric matrix
        conductivity_matrix=conductivity_matrix,
        # Skew-symmetric matrix
        active_transport_matrix=np.array(
            [
                [0, 0, 0, 0, 100, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [-100, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        )
        if case_flags["active_cooling"]
        else np.zeros((8, 8)),
    )
