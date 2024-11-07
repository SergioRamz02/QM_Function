import numpy as np
import matplotlib.pyplot as plt

# Constantes para el oscilador armónico cuántico
m = 1.0  # Masa (arbitraria)
hbar = 1.0  # Constante de Planck reducida (arbitraria)
omega = 1.0  # Frecuencia angular (arbitraria)

# Definir la función de densidad de probabilidad para el estado base
def psi_0_density(x, m, omega, hbar):
    """Densidad de probabilidad de la función de onda en el estado base del oscilador armónico cuántico."""
    normalization_factor = np.sqrt(m * omega / (np.pi * hbar))
    return normalization_factor * np.exp(-m * omega * x**2 / hbar)

# Rango de posiciones
x_values = np.linspace(-5, 5, 500)
density_values = psi_0_density(x_values, m, omega, hbar)**2  # Calcular la densidad de probabilidad

# Graficar la densidad de probabilidad
plt.figure(figsize=(8, 5))
plt.plot(x_values, density_values, label=r'$|\psi_0(x)|^2$')
plt.xlabel(r'Posición $x$')
plt.ylabel(r'Densidad de Probabilidad $|\psi_0(x)|^2$')
plt.title('Densidad de Probabilidad para el Estado Base del Oscilador Armónico Cuántico')
plt.legend()
plt.grid(True)
plt.show()
