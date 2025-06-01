import sys
from src.actividad_1 import plot_signals_in_groups
from src.actividad_2 import understanding_freq  # Asegúrate que esta importación sea válida

def main(options):
    if options[1] == "act_1":
        # Valores por defecto
        t_start, t_end, f = -1, 5, 2

        # Intentar leer argumentos si existen
        if len(options) >= 4:
            try:
                t_start = float(options[2])
                t_end = float(options[3])
            except ValueError:
                print("Error: Los valores de tiempo deben ser números. Usando valores por defecto [-1, 5].")

        if len(options) >= 5:
            try:
                f = float(options[4])
            except ValueError:
                print("Error: La frecuencia debe ser un número. Usando frecuencia por defecto 2 Hz.")

        plot_signals_in_groups(t_start, t_end, f)

    elif options[1] == "act_2":
        if len(options) > 2:
            understanding_freq(options[2])
        else:
            print("Please give a frequency. Example: python main.py act_2 2")
    else:
        print("Unknown option")

if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Please give an argument")
        print("Example (run activity 1): python main.py act_1")
        print("Example (run activity 1 with custom range and frequency): python main.py act_1 -1 5 3")
        print("Example (run activity 2): python main.py act_2 1")
