"""Transfer function for task2 and its parameters"""
from scipy import signal
import control

K = 12
T = 2
damp = 0.6


def transfer_func():
    return signal.TransferFunction([K], [T * T, 2 * T * damp, 1])  # k / ( T^2 * w^2 + [2Tξ]w + 1)


def control_tf(d=0.6):
    return control.TransferFunction([K], [T * T, 2 * T * d, 1])
