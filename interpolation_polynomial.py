import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import interp1d

# Предположим, что у нас есть следующие опытные данные координат точек
points = np.array([
    [1, 2, 3],
    [2, 3, 4],
    [3, 4, 5],
    [4, 5, 6],
    [5, 6, 7]
])

# Разделяем данные на отдельные координаты
x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

# Создаем функции интерполяции для каждой координаты
interp_x = interp1d(np.arange(points.shape[0]), x, kind='cubic')
interp_y = interp1d(np.arange(points.shape[0]), y, kind='cubic')
interp_z = interp1d(np.arange(points.shape[0]), z, kind='cubic')

# Генерируем новые точки для аппроксимации
num_points = 100
new_indices = np.linspace(0, points.shape[0] - 1, num_points)
new_x = interp_x(new_indices)
new_y = interp_y(new_indices)
new_z = interp_z(new_indices)

# Визуализация исходных точек и аппроксимированной кривой
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, color='red', label='Исходные точки')
ax.plot(new_x, new_y, new_z, color='blue', label='Аппроксимированная кривая')
ax.legend()
plt.show()