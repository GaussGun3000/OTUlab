import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
from w import transfer_func as tf



"""def wplot():
    t = np.arange(-1.0001e07, -0.9999e07, 10)
    plotter.plot(t, tf(t))
    plotter.show()
"""


def bode():
    stf = tf()  # init Transfer Function object
    w, mag, phase = signal.bode(stf)
    plt.figure()
    plt.title("АЧХ")
    plt.xlabel("w")
    plt.ylabel("А")
    plt.semilogx(w, mag)

    plt.figure()
    plt.title("ФЧХ")
    plt.xlabel("w")
    plt.ylabel("Ф")
    plt.semilogx(w, phase)
    plt.show()


def step_signal():
    t, y = signal.step(tf())
    plt.plot(t, y)
    plt.grid()
    plt.show()


def square_signal():
    t = np.linspace(0, 0.0000015, 100000)
    ss = 50 * signal.square(15000000 * t, 0.5)
    ss += abs(ss)
    # plt.plot(t, 100 * ss)
    tout, y, x = signal.lsim(tf(), ss, t)
    plt.plot(t, y)
    plt.grid(alpha=0.5)
    plt.show()


def wf():
    pass

"""
1. Составить математическую модель в дифференциальных уравнениях для RLC-цепи, в соответствии с вариантом задания.
2. Перейти от математической модели в дифференциальных уравнениях к передаточной функции.
3. Построить компьютерные модели. (на основе ДУ и ПФ). Использовать в качестве входного источника сигнала:
    3.1 Ступенчатый импульс (Step) со значением final value = Un (In), где n – номер варианта.
    3.2 Прямоугольный импульс (Pulse Generator) с амплитудным значением final value = Un (In), где n – номер варианта. (не менее 3 прямоугольных импульсов за все время симуляции.)
4. Получить переходные характеристики для каждой из построенных моделей при различных входных сигналах. Выполнить сравнительный анализ.
5. Построить ПФ объекта в MATLAB (Command Window) и получить следующие характеристики:
    - Переходная характеристика;
    - Логарифмические частотные характеристики;
    - Амплитудно-фазовая характеристика;
    - Расположение корней объекта на корневой плоскости.
    Проанализировать полученные характеристики.
"""