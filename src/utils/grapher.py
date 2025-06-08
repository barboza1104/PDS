import matplotlib.pyplot as plt

def continuous_plotter(t, x, fig_title, title, xlabel, ylabel):
    plt.figure()
    plt.plot(t, x)
    plt.title(fig_title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.xlim(min(t), max(t))
    plt.show()


def signal_plots(t_cont, x_cont, t_disc, x_disc, title):
    x_min = min(t_cont[0], t_disc[0])
    x_max = max(t_cont[-1], t_disc[-1])

    fig1, axs1 = plt.subplots(2, 1, figsize=(8, 6))
    axs1[0].plot(t_cont, x_cont, color='blue')
    axs1[0].set_title('Señal Continua')
    axs1[0].grid(True)
    axs1[0].set_xlim(x_min, x_max)

    axs1[1].stem(t_disc, x_disc, linefmt='k', markerfmt='ro', basefmt='none')
    axs1[1].set_title('Señal Discreta')
    axs1[1].grid(True)
    axs1[1].set_xlim(x_min, x_max)

    fig1.suptitle(title)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.plot(t_cont, x_cont, label='Continua', color='blue')
    ax2.stem(t_disc, x_disc, linefmt='k', markerfmt='ro', basefmt='none', label='Discreta')
    ax2.set_title('Señal Continua + Discreta')
    ax2.grid(True)
    ax2.legend()
    ax2.set_xlim(x_min, x_max)

    fig2.suptitle(title)
    plt.tight_layout()
    plt.show()

def compare_plotter(t_cont, x_cont, x_ref_cont, n_disc, x_disc, x_ref_disc, A, f, phi):
    import matplotlib.pyplot as plt

    fig, axs = plt.subplots(2, 1, figsize=(10, 6))

    axs[0].plot(t_cont, x_ref_cont, 'k--', label='Referencia: A=1, f=1Hz, ϕ=0')
    axs[0].plot(t_cont, x_cont, 'b', label=f'Modificada: A={A}, f={f}Hz, ϕ={phi} rad')
    axs[0].set_title('Señal Continua')
    axs[0].set_xlabel('Tiempo [s]')
    axs[0].set_ylabel('Amplitud')
    axs[0].legend()
    axs[0].grid(True)

    axs[1].stem(n_disc, x_ref_disc, linefmt='k--', markerfmt='ko', basefmt=' ', label='Referencia: A=1, f=1Hz, ϕ=0')
    axs[1].stem(n_disc, x_disc, linefmt='b-', markerfmt='bo', basefmt=' ', label=f'Modificada: A={A}, f={f}Hz, ϕ={phi} rad')
    axs[1].set_title('Señal Discreta')
    axs[1].set_xlabel('Tiempo [s]')
    axs[1].set_ylabel('Amplitud')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()
