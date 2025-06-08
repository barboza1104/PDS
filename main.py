import sys
import sys
from src.actividad_1 import plot_signals_in_groups
from src.actividad_2 import understanding_freq
from src.actividad_3 import analyze_signal_parameters
from src.actividad_4 import dac_analysis
def main(options):
    # Verificar que al menos se pasó una opción
    if len(options) < 2:
        print("Por favor proporciona una opción.")
        print("Ejemplos de uso:")
        print("  python main.py act_1")
        print("  python main.py act_1 -1 5 3")
        print("  python main.py act_2 2")
        print("  python main.py act_3 1 2 0.5")
        return

    opcion = options[1]

    if opcion == "act_1":
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

        print(f"Ejecutando actividad 1 con t_start={t_start}, t_end={t_end}, frecuencia={f} Hz")
        plot_signals_in_groups(t_start, t_end, f)

    elif opcion == "act_2":
        if len(options) > 2:
            try:
                freq = float(options[2])
                print(f"Ejecutando actividad 2 con frecuencia={freq} Hz")
                understanding_freq(freq)
            except ValueError:
                print("Error: La frecuencia debe ser un número.")
        else:
            print("Por favor proporciona una frecuencia. Ejemplo:")
            print("  python main.py act_2 2")

    elif opcion == "act_3":
        if len(options) < 5:
            print("Por favor proporciona amplitud, frecuencia y fase. Ejemplo:")
            print("  python main.py act_3 1 2 0.5")
        else:
            try:
                amplitude = float(options[2])
                frequency = float(options[3])
                phase = float(options[4])
                print(f"Ejecutando actividad 3 con amplitud={amplitude}, frecuencia={frequency}, fase={phase}")
                analyze_signal_parameters(amplitude, frequency, phase)
            except ValueError:
                print("Error: Asegúrate de que los valores sean numéricos (amplitud, frecuencia, fase)")
                
    elif opcion == "tarea_4":
        if len(options) < 3:
            print("Por favor proporciona el número de bits para el DAC.")
            print("Ejemplo: python main.py tarea_4 8")
            return
        try:
            n_bits = int(options[2])
            if n_bits <= 0:
                print("El número de bits debe ser un entero positivo.")
                return
        except ValueError:
            print("El número de bits debe ser un entero válido.")
            return

        dac_analysis(n_bits)

    else:
        print(f"Opción desconocida: {opcion}")
        print("Opciones válidas: act_1, act_2, act_3, tarea_4")

if __name__ == '__main__':
    main(sys.argv)