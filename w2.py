"""Transfer function for task2 and its parameters"""
import numpy as np
from scipy import signal
import control

K = 12
T = 2


def transfer_func(d=0.6):
    return signal.TransferFunction([K], [T * T, 2 * T * d, 1])  # k / ( T^2 * w^2 + [2Tξ]w + 1)


def control_tf(d=0.6):
    return control.TransferFunction([K], [T * T, 2 * T * d, 1])



