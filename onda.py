import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def wave_equation(num_steps, num_points, r):
    length = 1.0  # Longitud de la cuerda
    T = 1.0  # Tiempo total de simulación
    c = 1.0  # Velocidad de la onda
    delta_x = length / (num_points - 1)
    delta_t = T / num_steps

    # Inicialización de la malla
    u = np.zeros((num_points, num_steps + 1))

    # Condición inicial
    u[:, 0] = np.sin(np.pi * np.linspace(0, 1, num_points))

    # Condición inicial para el paso anterior (necesaria para el método de diferencias finitas en el tiempo)
    u[:, 1] = u[:, 0] + delta_t * np.sin(np.pi * np.linspace(0, 1, num_points))

    # Iteración temporal
    for j in range(1, num_steps):
        for i in range(1, num_points - 1):
            u[i, j + 1] = 2 * (1 - r**2) * u[i, j] + r**2 * (u[i + 1, j] + u[i - 1, j]) - u[i, j - 1]

    x = np.linspace(0, length, num_points)
    t = np.linspace(0, T, num_steps + 1)

    # Visualizacion
    X, T = np.meshgrid(x, t)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, u.T, cmap='viridis')
    ax.set_xlabel('Posición')
    ax.set_ylabel('Tiempo')
    ax.set_zlabel('Amplitud')
    ax.set_title('Evolución de la Onda en una Cuerda')
    plt.show()

num_points = 50  # Numero de puntos de la malla espacial
num_steps = 500  # Numero de pasos de tiempo
r = 0.01  # Numero de Courant

wave_equation(num_steps, num_points, r)