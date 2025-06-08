import numpy as np
from src.utils.grapher import compare_plotter

def analyze_signal_parameters(A, f, phi):
    A = float(A)
    f = float(f)
    phi = float(phi)

    # Tiempo continuo
    t = np.linspace(0, 2, 1000)
    x_cont = A * np.sin(2 * np.pi * f * t + phi)
    x_ref = np.sin(2 * np.pi * 1 * t)  # Referencia: A=1, f=1Hz, phi=0

    # Tiempo discreto
    Ts = 0.01
    n = np.arange(0, 2, Ts)
    x_disc = A * np.sin(2 * np.pi * f * n + phi)
    x_ref_disc = np.sin(2 * np.pi * 1 * n)

    compare_plotter(t, x_cont, x_ref, n, x_disc, x_ref_disc, A, f, phi)

