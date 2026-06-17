import numpy as np
import matplotlib.pyplot as plt

class RectangularBeam:
    """Representa una viga de sección rectangular."""
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    @property
    def moment_of_inertia_x(self) -> float:
        """Calcula el Momento de Inercia (I) en mm^4."""
        return (self.width * (self.height ** 3)) / 12

def plot_stress_distribution(beam: RectangularBeam, moment: float):
    """
    Grafica el diagrama de distribución de esfuerzos a lo largo del peralte.
    
    Args:
        beam (RectangularBeam): Instancia de la viga.
        moment (float): Momento flector en N-mm.
    """
    # 1. Definir el rango de 'y' desde la fibra inferior (-h/2) a la superior (h/2)
    h_half = beam.height / 2
    y_values = np.linspace(-h_half, h_half, 100)
    
    # 2. Calcular el esfuerzo para cada punto: sigma = (M * y) / I
    # Nota: y es la distancia desde el eje neutro.
    stresses = (moment * y_values) / beam.moment_of_inertia_x

    # 3. Configuración de la gráfica
    plt.figure(figsize=(8, 6))
    plt.plot(stresses, y_values, color='navy', linewidth=2, label='Distribución de Esfuerzos')
    
    # Dibujar el eje neutro
    plt.axhline(0, color='black', linestyle='--', linewidth=1, label='Eje Neutro')
    # Dibujar la línea vertical de referencia (esfuerzo cero)
    plt.axvline(0, color='gray', linewidth=0.8)

    # Añadir flechas representativas (opcional, para estética de ingeniería)
    for i in range(0, len(y_values), 10):
        plt.arrow(0, y_values[i], stresses[i], 0, 
                  head_width=1.5, head_length=abs(stresses.max())*0.05, 
                  fc='red' if stresses[i] > 0 else 'blue', 
                  ec='red' if stresses[i] > 0 else 'blue', alpha=0.5)

    # 4. Anotaciones y Estética
    plt.title(f'Diagrama de Distribución de Esfuerzos\nSección {beam.width}x{beam.height} mm', fontsize=12)
    plt.xlabel('Esfuerzo Normal $\sigma$ (MPa)', fontsize=10)
    plt.ylabel('Peralte de la viga (y) [mm]', fontsize=10)
    
    # Etiquetas de tensión/compresión
    plt.text(stresses.max(), h_half, f' Tracción Máx: {stresses.max():.2f} MPa', verticalalignment='bottom')
    plt.text(stresses.min(), -h_half, f' Compresión Máx: {stresses.min():.2f} MPa', horizontalalignment='right')

    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.show()

# --- Ejemplo de ejecución ---
if __name__ == "__main__":
    # Definimos una viga de 50mm de ancho y 150mm de alto
    mi_viga = RectangularBeam(width=50, height=150)
    
    # Aplicamos un momento de 10 kNm (10,000,000 N-mm)
    momento_diseno = 10_000_000 
    
    plot_stress_distribution(mi_viga, momento_diseno)