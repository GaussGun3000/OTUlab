"""Transfer functions for task2 and its default parameters"""
import numpy as np
from scipy import signal
import control

K = 12
T = 2


def transfer_func(d=0.6, t=T):
    return signal.TransferFunction([K], [t * t, 2 * t * d, 1])  # k / ( T^2 * s^2 + [2Tξ]s + 1)


def control_tf(d=0.6):
    return control.TransferFunction([K], [T * T, 2 * T * d, 1])



