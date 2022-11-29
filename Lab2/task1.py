"""
h = 9;     q = 4;

ДУ: dh/dt = 1 / S * (Q(t)-q(t));
ПФОС: W(s) = k = 1;
1. Построить систему управления с использованием ПИ и ПИД регулятора, который бы обеспечивал e[уст]→0. Получить для с
системы с каждым видом регулятора переходную характеристику и частотные характеристики.
Сравнить полученные результаты и сделать выводы.
2. Определить параметры ПИД-регулятора при наименьшем перерегулировании в системе. При полученных параметрах
 определить запасы устойчивости по амплитуде и фазе, степень устойчивости и колебательности. Сделать выводы.
3. Определить параметры ПИД-регулятора при наименьшем времени регулирования в системе. При полученных
 параметрах определить запасы устойчивости по амплитуде и фазе, степень устойчивости и колебательности.
 Сделать выводы.
"""
import time

from simple_pid import PID
import matplotlib.pyplot as plt
import numpy as np

WATER_TARGET_LEVEL = 9
WATER_OUTLET_RATE = 4


class WaterTank:
    def __init__(self):
        self.water_level = 0

    def update(self, inlet: float, dt: float):
        """
        Update state of the object based on water inlet amount as control input

        :param inlet: water inlet amount (m^3/s)
        :param dt: time span in seconds
        :return: None
        """
        if inlet >= 0:
            self.water_level += inlet * dt
        else:
            raise ValueError(f"WaterTank.update(): Value of inlet param can not be negative (got {inlet})")
        self.water_level -= WATER_OUTLET_RATE * dt if self.water_level - WATER_OUTLET_RATE * dt >= 0 else 0


def run():
    tank_pi = WaterTank()
    tank_pid = WaterTank()

    pi_controller = PID(1, 0.5, 0, setpoint=WATER_TARGET_LEVEL)
    pid_controller = PID(1, 0.5, 0.5, setpoint=WATER_TARGET_LEVEL)
    pi_controller.output_limits = (0, 20)
    pid_controller.output_limits = (0, 20)

    y_pi, y_pid = [], []
    values = 1000
    tf = 20
    t = np.linspace(0, tf, values + 1)
    dt = tf / values

    for ct in t:
        inlet = pi_controller(tank_pi.water_level, dt=dt)
        tank_pi.update(inlet, dt=dt)

        inlet = pid_controller(tank_pid.water_level, dt=dt)
        tank_pid.update(inlet, dt=dt)
        y_pi += [tank_pi.water_level]
        y_pid += [tank_pid.water_level]

    plt.plot(t, y_pi, color='red', linestyle="--")
    plt.axhline(y=9)
    plt.xlabel('time')
    plt.ylabel('level')
    plt.show()
    input("Press enter to continue . . .")
    plt.figure()
    plt.plot(t, y_pid, color='red', linestyle="--")
    plt.axhline(y=9)
    plt.xlabel('time')
    plt.ylabel('level')
    plt.show()
