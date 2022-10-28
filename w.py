from scipy import signal
L = 0.0000015  # inductance
R = 15   # resistance
"""Transfer function"""


def transfer_func() -> signal.TransferFunction:
    return signal.TransferFunction([1], [L, R])  # 1 / (L * s + R)

