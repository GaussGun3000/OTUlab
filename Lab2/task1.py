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
from simple_pid import PID
import matplotlib.pyplot as plt


WATER_TARGET_LEVEL = 9
WATER_OUTLET_RATE = 4


class WaterTank:
    def __init__(self):
        self.water_level = WATER_TARGET_LEVEL

    def update(self, inlet: int, dt: float):
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
        self.water_level -= WATER_OUTLET_RATE * dt


def run():
    tank = WaterTank()
    pi_controller = PID(1, 1, 0, setpoint=tank.water_level)
    pi_controller.output_limits = (0, 20)

