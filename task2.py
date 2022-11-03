import matplotlib.pyplot as plt
from scipy import signal
from w2 import transfer_func as tf, K, T, damp
import control


def freq_properties():
    """
    Draw bode, step response, Pole-zero map and nyquist diagram.
    """
    w, mag, phase = signal.bode(tf())
    plt.figure()
    plt.grid()
    plt.title("АЧХ")
    plt.xlabel("w")
    plt.ylabel("А")
    plt.semilogx(w, mag)
    plt.show()
    input("Press enter to continue . . .")

    plt.figure()
    plt.grid()
    plt.title("ФЧХ")
    plt.xlabel("w")
    plt.ylabel("Ф")
    plt.semilogx(w, phase)
    plt.show()
    input("Press enter to continue . . .")

    plt.figure()
    plt.title("ПХ")
    t, y = signal.step(tf())
    plt.plot(t, y)
    plt.grid()
    plt.show()
    input("Press enter to continue . . .")

    ctf = control.TransferFunction([K], [T * T, 2 * T * damp, 1])
    plt.figure()
    control.nyquist_plot([ctf, ], plot=True)
    plt.title("АФХ")
    plt.show()
    input("Press enter to continue . . .")


"""
k=12;   T=2;   ξ=0.6

Для звена вида <task2_formula.png>
определить переходную и частотные характеристики (АФХ и ЛЧХ) при выбранных значениях (см. варианты задания)
параметров T, ξ, привести графики.
    Провести исследование характеристик звена, состоящее в следующем:
1. Проанализировать движение корней (траекторий корней) ХП на комплексной плоскости при изменении
параметра ξ, привести графики.
2. Построить график зависимости резонансного пика АЧХ от коэффициента демпфирования в пределах 0 <= ξ <=1.
3. Построить график зависимости резонансной частоты ωp от постоянной времени Т при выбранном значении ξ.
4. Определить экспериментально оптимальное значение коэффициента демпфирования ξ=ξопт из условия минимума
времени tp затухания процесса (принять за tp время, начиная с которого переходная характеристика остается
в пределах ± 5% от установившегося значения). Как располагаются на комплексной плоскости корни ХП при
ξ=ξопт ? Чему равна высота пика ЛАЧХ?
5. Определить переходную и частотные характеристики (АФХ и ЛЧХ) при изменении знака коэффициента демпфирования 
ξ на -ξ, привести графики.

"""