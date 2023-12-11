import numpy as np
import matplotlib.pyplot as plt

def heat_equation(num_steps, num_points, r):
    length = 1.0  # Longitud de la barra
    T = 1.0  # Tiempo total de simulación
    alpha = 0.01  # Coeficiente de difusión térmica
    delta_x = length / (num_points - 1)
    delta_t = T / num_steps

    # Inicialización de la malla
    u = np.zeros((num_points, num_steps + 1))

    # Condición inicial
    u[:, 0] = np.sin(np.pi * np.linspace(0, 1, num_points))

    # Iteracion temporal
    for j in range(0, num_steps):
        for i in range(1, num_points - 1):
            u[i, j + 1] = (1 - 2 * r) * u[i, j] + r * (u[i + 1, j] - 2 * u[i, j] + u[i - 1, j])

    x = np.linspace(0, length, num_points)
    t = np.linspace(0, T, num_steps + 1)

    # Visualizacion
    X, T = np.meshgrid(x, t)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, T, u.T, cmap='viridis')
    ax.set_xlabel('Posición')
    ax.set_ylabel('Tiempo')
    ax.set_zlabel('Temperatura')
    ax.set_title('Evolución de la Temperatura en una Barra')
    plt.show()

# Parámetros de la simulación
num_points = 50  # Numero de puntos de la malla espacial
num_steps = 500  # Numero de pasos de tiempo
r = 0.01  # Número de Courant

# Resolver la ecuación de calor
heat_equation(num_steps, num_points, r)