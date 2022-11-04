import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from w2 import transfer_func as tf, control_tf as ctf
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

    plt.figure()
    control.nyquist_plot([ctf(), ], plot=True)
    plt.title("АФХ")
    plt.grid(False)
    plt.xlim(left=0)
    plt.show()
    input("Press enter to continue . . .")


def zeros_graph():
    plot = plt.figure()
    damp_list = np.linspace(0, 1, 30)
    control.pzmap(ctf(0), plot=True, title='Карта нулей и полюсов')
    damp_list = damp_list[1:]
    for damp in damp_list:
        zeroes, poles = control.pzmap(ctf(damp), plot=False, title='Карта нулей и полюсов')
        x = [elem.real for elem in zeroes]
        y = [elem.imag for elem in zeroes]
        print(poles, zeroes)
        plt.scatter(x, y, marker='x')
    plt.show()
    input("Press enter to continue . . .")


def freq_damp_graph():
    damp_list = np.linspace(0, 1, 1000)
    max_mag = list()
    for damp in damp_list:
        w, mag, phase = signal.bode(tf(damp))
        max_mag.append(max(mag))
    plt.plot(damp_list, max_mag)
    plt.xlabel('ξ')
    plt.ylabel('R')
    plt.title('Зависимость резонансного пика АЧХ от ξ')
    plt.grid()
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