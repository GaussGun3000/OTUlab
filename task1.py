import matplotlib.pyplot as plt
from scipy import signal
import numpy as np
import ss_simulation
from w import transfer_func as tf, L, R
import control


def freq_properties():
    """
    Draw bode, step response, Pole-zero map and nyquist diagram.
    """
    stf = tf()  # init Transfer Function object
    w, mag, phase = signal.bode(stf)
    plt.figure()
    plt.title("АЧХ")
    plt.grid()
    plt.semilogx(w, mag)
    plt.show()
    input("Press enter to continue . . .")

    plt.figure()
    plt.title("ФЧХ")
    plt.grid()
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

    plot = plt.figure()
    ctf = control.TransferFunction([1], [L, R])
    control.pzmap(ctf, plot=plot, title='Карта нулей и полюсов')
    plt.grid(False)
    plt.show()
    input("Press enter to continue . . .")

    plt.figure()
    control.nyquist_plot([ctf, ], plot=True)
    plt.grid(False)
    plt.title("АФХ")
    plt.xlim(left=0)
    plt.show()

def step_signal(plot):
    """Draw step response"""
    t, y = signal.step(tf())
    plot.plot(t, 100 * y)
    plot.grid()
    plot.legend(['модель ПФ'], loc=4)


def square_signal(plot):
    """Draw square signal response"""
    t = np.linspace(0, 0.000004, 1000)
    ss = 50 * signal.square(6000000 * t, 0.5)
    ss += abs(ss)
    tout, y, x = signal.lsim(tf(), ss, t)
    plot.plot(t, y)
    plot.grid(alpha=0.5)
    plot.legend(['модель ПФ'], loc=4)


def run():
    """
    Run step and square signal simulations in both TF and DE models and plot the results
    """

    plot = ss_simulation.de_signal_simulation(repeats=1, color='r')  # step signal
    plot.set_xlim(0.0, 7e-7)
    step_signal(plot.twinx())

    plot1 = ss_simulation.de_signal_simulation(T=0.000001045, repeats=4, color='r', subplot=312)  # square signal
    square_signal(plot1.twinx())

    plt.show()
    input("Press enter to continue . . .")


def run_all():
    run()
    freq_properties()

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