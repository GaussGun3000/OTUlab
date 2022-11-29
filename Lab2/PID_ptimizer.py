import numpy as np


def optimise_pid(optimised_prop: str):
    """
    Tunes PID to suit chosen priority: better speed, more robustness or optimal performance

    :param optimised_prop: Property to be optimised for: "speed", "stability", or "optimal"
    :return:
    """
    rp = np.linspace(0, 2, 200)  # Proportional coefficient range
    ri = np.linspace(0, 2, 200)  # Integral coefficient range
    if optimised_prop == 'speed':
        pass


def optimise_pi():
    pass
