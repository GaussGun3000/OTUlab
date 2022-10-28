"""Simulation of circtuit response to repeated square signal"""

import numpy as np
import matplotlib.pyplot as plt

# Input voltage amplitude
AMPLITUDE = 100.0

# Active components
r = 15.0

# Reactive components=
L = 0.0000015

# Time components
T = 0.0000015
t0 = 0.0
step = T/10000
tf = T * 5

steps = int(tf/step)

il = []
y = []

# Input voltage
def E(t):
    n = int(t/T)
    if (t >= n*T) and (t <= n*T + T/2):
        return AMPLITUDE
    else:
        return 0.0


def dIl_dt(t):
    return float((1.0 / L) * (E(t) - r * il[int(t / step)]))


time = np.arange(t0, tf, step)


for i in range(0, steps, 1):
    y.append(E(time[i]))

#Start condition
il.append(0.0)


#Euler method
for i in range(1, steps, 1):
    il.append(il[i-1] + step * dIl_dt(time[i-1]))


plt.figure("charts")
e = plt.subplot(311)
e.plot(time, y)
e.set_xlabel('time (s)')
e.set_ylabel('E(t), (V)', color='b')
plt.grid(True)

IL = plt.subplot(312)
IL.plot(time, il, 'r')
IL.set_ylabel('Il(t), (A)', color='r')
plt.grid(True)
plt.show()