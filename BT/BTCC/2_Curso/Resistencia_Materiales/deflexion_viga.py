import numpy as np
import matplotlib.pyplot as plt

def plot_beam_deflection(L: float, a: float, P: float, E: float, I: float):
    """
    Calcula y grafica la deflexión de una viga simplemente apoyada con carga puntual.

    Args:
        L (float): Longitud total de la viga (mm).
        a (float): Distancia desde el apoyo izquierdo a la carga (mm).
        P (float): Magnitud de la carga puntual (N).
        E (float): Módulo de elasticidad del material (MPa o N/mm^2).
        I (float): Momento de inercia de la sección (mm^4).
    """
    b = L - a
    x_values = np.linspace(0, L, 500)
    deflection = []

    # Cálculo de la deflexión punto a punto (Ecuaciones de la elástica)
    for x in x_values:
        if x <= a:
            # Fórmula para el tramo izquierdo
            v = (P * b * x) / (6 * E * I * L) * (L**2 - b**2 - x**2)
        else:
            # Fórmula para el tramo derecho
            v = (P * a * (L - x)) / (6 * E * I * L) * (L**2 - a**2 - (L - x)**2)
        deflection.append(-v) # Negativo para representar descenso

    deflection = np.array(deflection)
    max_deflection = min(deflection)
    x_max_def = x_values[np.argmin(deflection)]

    # --- Configuración de la Gráfica ---
    plt.figure(figsize=(12, 5))
    
    # Dibujar la viga deformada
    plt.plot(x_values, deflection, color='tab:blue', linewidth=3, label='Curva Elástica')
    
    # Dibujar la línea original de la viga (sin carga)
    plt.axhline(0, color='black', linestyle='-', linewidth=2)

    # Representación de los apoyos (triángulos)
    plt.plot([0], [0], '^', markersize=15, color='black', label='Apoyo Fijo')
    plt.plot([L], [0], '^', markersize=15, color='gray', label='Apoyo Móvil')

    # Representación de la carga puntual (flecha)
    plt.annotate('', xy=(a, 0), xytext=(a, 5),
                 arrowprops=dict(facecolor='red', shrink=0.05, width=2))
    plt.text(a, 6, f'P = {P/1000:.1f} kN', color='red', ha='center', fontweight='bold')

    # Marcar la deflexión máxima
    plt.plot(x_max_def, max_deflection, 'ro')
    plt.annotate(f'f_max: {abs(max_deflection):.2f} mm', 
                 xy=(x_max_def, max_deflection), 
                 xytext=(x_max_def, max_deflection - 5),
                 ha='center', arrowprops=dict(arrowstyle='->'))

    # Estética y etiquetas
    plt.title(f'Análisis de Deflexión en Viga de {L/1000:.2f} m', fontsize=14)
    plt.xlabel('Longitud de la viga (x) [mm]', fontsize=12)
    plt.ylabel('Deflexión (v) [mm]', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Invertir eje Y para que la flecha hacia abajo sea visualmente intuitiva 
    # (o simplemente usar valores negativos como ya se hizo)
    plt.ylim(max_deflection - 10, 15)
    
    plt.legend()
    plt.tight_layout()
    plt.show()

# --- Ejemplo de uso técnico ---
if __name__ == "__main__":
    # Datos para una viga de acero IPN 200
    L_viga = 6000           # 6 metros
    posicion_carga = 3000   # Carga al centro (3m)
    carga_P = 25000         # 25 kN
    
    # Propiedades del Acero y la sección
    E_acero = 210000        # MPa
    # Ejemplo: Inercia de un perfil rectangular de 10x20cm
    # I = (100 * 200^3) / 12
    I_seccion = (100 * 200**3) / 12 
    
    plot_beam_deflection(L_viga, posicion_carga, carga_P, E_acero, I_seccion)