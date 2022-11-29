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

WATER_TARGET_LEVEL = 9


class WaterTank:
    def __init__(self):
        self.water_level = WATER_TARGET_LEVEL

    def update(self, inlet: int, dt: float):
        """
        Update state of the object based on water inlet amount as control input

        :param inlet: water inlet amount (m^3/s)
        :param dt: time span in seconds
        :return:
        """
        if inlet >= 0:
            pass
        else:
            raise ValueError(f"WaterTank.update(): Value of inlet param can not be negative (got {inlet})")


def run():
    pass