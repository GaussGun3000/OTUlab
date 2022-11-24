"""
k=12;   T=2;   ξ=0.6

Для звена вида <task2_formula.png>
определить переходную и частотные характеристики (АФХ и ЛЧХ) при выбранных значениях (см. варианты задания)
параметров T, ξ, привести графики.
    Провести исследование характеристик звена, состоящее в следующем:
+1. Проанализировать движение корней (траекторий корней) ХП на комплексной плоскости при изменении
параметра ξ, привести графики.
+2. Построить график зависимости резонансного пика АЧХ от коэффициента демпфирования в пределах 0 <= ξ <= 1.
+3. Построить график зависимости резонансной частоты ωp от постоянной времени Т при выбранном значении ξ.
+4. Определить экспериментально оптимальное значение коэффициента демпфирования ξ=ξопт из условия минимума
времени tp затухания процесса (принять за tp время, начиная с которого переходная характеристика остается
в пределах ± 5% от установившегося значения). Как располагаются на комплексной плоскости корни ХП при
ξ=ξопт ? Чему равна высота пика ЛАЧХ?
+5. Определить переходную и частотные характеристики (АФХ и ЛЧХ) при изменении знака коэффициента демпфирования
ξ на -ξ, привести графики.

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from w2 import transfer_func as tf, control_tf as ctf
import control


DAMP = 0.6


def pz_map(damp=DAMP):
    """
    Draw and display pole-zero map of TF with set damp coefficient

    :param damp: damping coefficient (default = 0.6)
    """
    plt.figure()
    control.pzmap(ctf(damp), plot=True, title='Карта нулей и полюсов')
    plt.show()
    input("Press enter to continue . . .")


def freq_properties(damp=DAMP):
    """
    Draw bode, step response, Pole-zero map and nyquist diagram.

    :param damp: damping coefficient (default = 0.6)
    """
    w, mag, phase = signal.bode(tf(damp))
    plt.figure()
    plt.grid()
    plt.title("АЧХ")
    plt.semilogx(w, mag)
    plt.show()
    input("Press enter to continue . . .")

    plt.figure()
    plt.grid()
    plt.title("ФЧХ")
    plt.semilogx(w, phase)
    plt.show()
    input("Press enter to continue . . .")

    plt.figure()
    plt.title("ПХ")
    t, y = signal.step(tf(damp), T=np.linspace(0, 100, 2000))
    plt.plot(t, y)
    plt.grid()
    plt.show()
    input("Press enter to continue . . .")

    plt.figure()
    control.nyquist_plot([ctf(damp), ], plot=True)
    plt.title("АФХ")
    plt.grid(False)
    plt.show()
    input("Press enter to continue . . .")


def zeros_graph():
    """Pole-Zero maps for different damp coefficients"""
    plt.figure()
    damp_list = np.linspace(0, 1, 30)
    control.pzmap(ctf(0), plot=True, title='Карта нулей и полюсов')
    damp_list = damp_list[1:]
    for damp in damp_list:
        zeroes, poles = control.pzmap(ctf(damp), plot=False, title='Карта нулей и полюсов')
        x = [elem.real for elem in zeroes]
        y = [elem.imag for elem in zeroes]
        plt.scatter(x, y, marker='x')
    plt.show()
    input("Press enter to continue . . .")


def ampl_damp_graph():
    """Resonant amplitude peaks for different damp coefficients"""
    damp_list = np.linspace(0, 1, 1000)
    max_mag = list()
    for damp in damp_list:
        w, mag, phase = signal.bode(tf(damp))
        max_mag.append(max(mag))
    plt.plot(damp_list, max_mag)
    plt.title('Зависимость резонансного пика АЧХ от ξ')
    plt.grid()
    plt.show()
    input("Press enter to continue . . .")


def res_freq_graph():
    """Resonant frequencies for different T coefficients"""
    t_list = np.linspace(0, 3, 1000)
    max_f = np.array(.0)
    for t in t_list:
        w, mag, phase = signal.bode(tf(DAMP, t))
        index = np.where(mag == mag.max())[0][0]
        max_f = np.append(max_f, w[index])
    plt.plot(t_list, max_f[1:])
    plt.title('Зависимость резонансной частоты от T')
    plt.grid()
    plt.show()
    input("Press enter to continue . . .")


def optimal_damp():
    """Optimal damp coefficient calculation based on 5% criteria"""
    damp_list = np.linspace(0, 1, 1000)
    custom_t = np.linspace(0, 50, 400)
    min_t = np.inf
    opt_d = 0
    EST = 12  # established step response value
    for damp in damp_list:
        t, y = signal.step(tf(damp), T=custom_t)
        range5 = np.where(y <= 0.95 * EST)[0]
        range5 = np.append(range5, np.where(y >= 1.05 * EST)[0])
        time = t[range5.max()]
        plt.plot(t, y)
        if time < min_t:
            min_t = time
            opt_d = damp
    print(f"Optimal damp coefficient = {opt_d}")
    plt.show()
    return opt_d


def magnitude_peak(damp):
    w, mag, phase = signal.bode(tf(damp))
    print(f"Optimal damp magnitude peak = {max(mag)}\n")


def run_all():
    """Run all the functions to display plots and information required for task 2"""
    freq_properties()  # task
    zeros_graph()  # 1
    ampl_damp_graph()  # 2
    res_freq_graph()  # 3
    opt_d = optimal_damp()  # 4
    pz_map(opt_d)  # 4
    magnitude_peak(opt_d)  # 4
    freq_properties(-DAMP)  # 5
