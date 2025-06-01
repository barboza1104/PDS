import numpy as np
from scipy.signal import sawtooth, square
from src.utils.grapher import signal_plots

def plot_signals_in_groups(t_start=-1, t_end=5, f=2):
    Ts = 0.05  # Periodo de muestreo

    # Tiempo continuo y discreto
    t_cont = np.linspace(t_start, t_end, 1000)
    t_disc = np.arange(t_start, t_end + Ts, Ts)

    # Señal senoidal
    x1_cont = np.sin(2 * np.pi * f * t_cont)
    x1_disc = np.sin(2 * np.pi * f * t_disc)
    signal_plots(t_cont, x1_cont, t_disc, x1_disc, rf'$x_1(t) = \sin(2\pi \cdot {f} t)$')

    # Señal exponencial con escalón unitario u(t)
    x2_cont = np.exp(-2 * t_cont) * (t_cont >= 0)
    x2_disc = np.exp(-2 * t_disc) * (t_disc >= 0)
    signal_plots(t_cont, x2_cont, t_disc, x2_disc, r'$x_2(t) = e^{-2t} u(t)$')

    # Señal triangular periódica
    x3_cont = sawtooth(2 * np.pi * f * t_cont, width=0.5)
    x3_disc = sawtooth(2 * np.pi * f * t_disc, width=0.5)
    signal_plots(t_cont, x3_cont, t_disc, x3_disc, rf'$x_3(t) = tri(t, {f})$')

    # Señal cuadrada periódica
    x4_cont = square(2 * np.pi * f * t_cont)
    x4_disc = square(2 * np.pi * f * t_disc)
    signal_plots(t_cont, x4_cont, t_disc, x4_disc, rf'$x_4(t) = sq(t, {f})$')

__all__ = ['plot_signals_in_groups']
