from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parent / "graficos_material_alumno"
OUT.mkdir(exist_ok=True)


def grafico_vectores():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_title("Representacion de una fuerza como vector")

    origen = (0, 0)
    fx, fy = 6, 4

    ax.arrow(*origen, fx, fy, head_width=0.25, head_length=0.35, fc="tab:red", ec="tab:red", linewidth=2)
    ax.arrow(*origen, fx, 0, head_width=0.18, head_length=0.22, fc="tab:blue", ec="tab:blue", linewidth=1.8)
    ax.arrow(fx, 0, 0, fy, head_width=0.18, head_length=0.22, fc="tab:green", ec="tab:green", linewidth=1.8)

    ax.plot([fx, fx], [0, fy], linestyle="--", color="gray")
    ax.text(fx / 2, -0.45, "Fx", color="tab:blue", ha="center")
    ax.text(fx + 0.35, fy / 2, "Fy", color="tab:green", va="center")
    ax.text(fx / 2 + 0.4, fy / 2 + 0.3, "F", color="tab:red", fontweight="bold")
    ax.text(2.4, 0.5, "direccion", color="black")
    ax.text(5.5, 3.7, "sentido", color="black")

    ax.set_xlim(-0.5, 7.5)
    ax.set_ylim(-1, 5.5)
    ax.set_xlabel("Eje x")
    ax.set_ylabel("Eje y")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.set_aspect("equal", adjustable="box")
    fig.tight_layout()
    fig.savefig(OUT / "01_vector_fuerza.png", dpi=180)
    plt.close(fig)


def grafico_viga_cargas():
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.set_title("Viga simplemente apoyada con carga puntual")

    L = 8
    carga_x = 4

    ax.plot([0, L], [0, 0], color="black", linewidth=3)
    ax.plot([0], [0], "^", markersize=14, color="black")
    ax.plot([L], [0], "^", markersize=14, color="gray")

    ax.annotate("", xy=(carga_x, 0.15), xytext=(carga_x, 2.0),
                arrowprops=dict(arrowstyle="-|>", color="red", lw=2.2))
    ax.text(carga_x + 0.12, 1.25, "P", color="red", fontweight="bold")

    ax.annotate("", xy=(0, 1.1), xytext=(0, 0.05),
                arrowprops=dict(arrowstyle="-|>", color="tab:blue", lw=2))
    ax.annotate("", xy=(L, 1.1), xytext=(L, 0.05),
                arrowprops=dict(arrowstyle="-|>", color="tab:green", lw=2))
    ax.text(-0.25, 1.15, "RA", color="tab:blue")
    ax.text(L - 0.1, 1.15, "RB", color="tab:green")

    ax.text(1.6, -0.45, "L/2", color="black")
    ax.text(5.6, -0.45, "L/2", color="black")
    ax.set_xlim(-0.8, 8.8)
    ax.set_ylim(-0.8, 2.4)
    ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUT / "02_viga_carga_reacciones.png", dpi=180, bbox_inches="tight")
    plt.close(fig)


def grafico_esfuerzos_flexion():
    fig, ax = plt.subplots(figsize=(8, 6))
    h = 14
    y = np.linspace(-h / 2, h / 2, 100)
    sigma = 1.4 * y

    ax.plot(sigma, y, color="navy", linewidth=2.2)
    ax.axhline(0, color="black", linestyle="--", linewidth=1)
    ax.axvline(0, color="gray", linewidth=1)

    for i in range(0, len(y), 12):
        color = "tab:red" if sigma[i] > 0 else "tab:blue"
        ax.arrow(0, y[i], sigma[i], 0, head_width=0.35, head_length=0.25, fc=color, ec=color, alpha=0.65)

    ax.text(sigma.max() + 0.2, y.max() - 0.3, "Traccion", color="tab:red")
    ax.text(sigma.min() - 1.2, y.min() + 0.3, "Compresion", color="tab:blue")
    ax.text(0.15, 0.3, "Eje neutro", color="black")

    ax.set_title("Distribucion lineal de esfuerzos por flexion")
    ax.set_xlabel("Esfuerzo normal")
    ax.set_ylabel("Altura de la seccion")
    ax.grid(True, linestyle=":", alpha=0.6)
    fig.tight_layout()
    fig.savefig(OUT / "03_distribucion_esfuerzos_flexion.png", dpi=180)
    plt.close(fig)


def grafico_deflexion():
    fig, ax = plt.subplots(figsize=(10, 4))
    x = np.linspace(0, 10, 400)
    y = -0.18 * x * (10 - x)
    y = y / abs(y.min()) * 1.6

    ax.plot(x, np.zeros_like(x), color="black", linewidth=2.5, label="Viga sin deformar")
    ax.plot(x, y, color="tab:purple", linewidth=2.8, label="Curva elastica")
    ax.plot([0], [0], "^", markersize=12, color="black")
    ax.plot([10], [0], "^", markersize=12, color="gray")
    i = np.argmin(y)
    ax.plot(x[i], y[i], "o", color="tab:red")
    ax.annotate("Deflexion maxima", xy=(x[i], y[i]), xytext=(x[i] + 0.8, y[i] - 0.35),
                arrowprops=dict(arrowstyle="->", color="tab:red"), color="tab:red")

    ax.set_title("Deflexion de una viga simplemente apoyada")
    ax.set_xlabel("Longitud de la viga")
    ax.set_ylabel("Flecha")
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend()
    fig.tight_layout()
    fig.savefig(OUT / "04_deflexion_viga.png", dpi=180)
    plt.close(fig)


if __name__ == "__main__":
    grafico_vectores()
    grafico_viga_cargas()
    grafico_esfuerzos_flexion()
    grafico_deflexion()
    print(f"Graficos generados en: {OUT}")
