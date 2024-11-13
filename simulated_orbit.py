import numpy as np
import matplotlib.pyplot as plt

# Constantes y parámetros iniciales
G = 6.67430e-11  # Constante gravitacional
M_sun = 1.989e30  # Masa del Sol en kg
c = 3e8  # Velocidad de la luz en m/s

# Parámetros de Mercurio (en metros y segundos)
r_min = 4.6e10  # Distancia mínima de Mercurio al Sol (perihelio)
v_init = 4.79e4  # Velocidad inicial de Mercurio en m/s
dt = 1000  # Paso temporal en segundos
num_steps = 100000  # Incrementar pasos para observar más precesión

# Posiciones y velocidades iniciales
r = np.array([r_min, 0])
v = np.array([0, v_init])

# Configuración de listas para almacenar la órbita
positions_x = []
positions_y = []

def acceleration(r, exaggeration_factor=10):
    # Distancia entre Mercurio y el Sol
    distance = np.linalg.norm(r)
    
    # Potencial con corrección relativista exagerada para mostrar la precesión
    factor_rel = 1 + (3 * G * M_sun) / (c**2 * distance) * exaggeration_factor
    acc = -G * M_sun * r / distance**3 * factor_rel
    return acc

# Simulación de la órbita
for step in range(num_steps):
    # Actualizar posiciones y velocidades (integración de Verlet)
    r += v * dt + 0.5 * acceleration(r) * dt**2
    v += acceleration(r) * dt

    # Guardar posiciones
    positions_x.append(r[0])
    positions_y.append(r[1])

# Convertir la trayectoria en arrays para graficar
positions_x = np.array(positions_x)
positions_y = np.array(positions_y)

# Graficar la órbita de Mercurio con precesión más notoria
plt.figure(figsize=(8, 8))
plt.plot(positions_x, positions_y, color='blue', label='Órbita de Mercurio')
plt.plot(0, 0, 'yo', markersize=10, label='Sol')  # Sol en amarillo
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.title('Órbita de Mercurio con Precesión Exagerada')
plt.axis('equal')
plt.grid(True)
plt.show()

# Cálculo de precesión en segundos por siglo (ajustado)
precesion_total_arcsec = (3 * G * M_sun) / (r_min * c**2) * 206265 * 100  # segundos de arco
precesion_total_sec = precesion_total_arcsec / 3600  # Conversión a segundos por siglo

precesion_total_arcsec, precesion_total_sec 
