
import numpy as np
import matplotlib.pyplot as plt

def dac_analysis(n_bits):
    V_FS = 5.0  # Voltaje de escala completa (V)

    num_levels = 2 ** n_bits
    step_size = V_FS / (num_levels - 1)
    resolution_percent = (step_size / V_FS) * 100

    print(f"DAC de {n_bits} bits")
    print(f"Número total de niveles: {num_levels}")
    print(f"Tamaño del paso (LSB): {step_size:.6f} V")
    print(f"Resolución porcentual: {resolution_percent:.6f} %")

    digital_inputs = np.arange(num_levels)
    analog_outputs = digital_inputs * step_size

    plt.figure(figsize=(8,5))
    plt.step(digital_inputs, analog_outputs, where='post', color='blue')
    plt.title(f'Salida analógica de un DAC de {n_bits} bits')
    plt.xlabel('Entrada digital (decimal)')
    plt.ylabel('Voltaje de salida (V)')
    plt.grid(True)
    plt.xlim(0, num_levels - 1)
    plt.ylim(0, V_FS)
    plt.tight_layout()
    plt.show()
