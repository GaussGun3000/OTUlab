"""
Simulation of circtuit response to repeated square signal (based on Differential equation)
Credit: https://habr.com/ru/post/323590/
"""

import numpy as np
import matplotlib.pyplot as plt

# Input voltage amplitude
AMPLITUDE = 100.0

# Active components
r = 15.0

# Reactive components=
L = 0.0000015


def de_signal_simulation(T=0.0000015, repeats=5, color='b', subplot=311):
    # Time components
    t0 = 0.0
    step = T / 10000
    tf = T * repeats

    steps = int(tf / step)

    il = []
    y = []

    # Input voltage
    def E(t):
        n = int(t / T)
        if (t >= n * T) and (t <= n * T + T / 2):
            return AMPLITUDE
        else:
            return 0.0

    def dIl_dt(t):
        return float((1.0 / L) * (E(t) - r * il[int(t / step)]))

    time = np.arange(t0, tf, step)

    for i in range(0, steps, 1):
        y.append(E(time[i]))

    # Start condition
    il.append(0.0)

    # Euler method
    for i in range(1, steps, 1):
        il.append(il[i - 1] + step * dIl_dt(time[i - 1]))

    plot = plt.subplot(subplot)
    plot.plot(time, il, color)
    # plt.xlim(0.0, 7e-7)
    plt.grid(True)
    plot.legend(['DE model'], loc = 5)
    return plot



