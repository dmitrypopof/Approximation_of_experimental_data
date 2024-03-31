import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Задаем 6 контрольных точек в трехмерном пространстве
control_points = np.array([
    [0, 0, 0],
    [1, 2, 3],
    [2, -1, 4],
    [3, 0, 2],
    [4, 2, 0],
    [5, 5, 5]
])

# Функция для расчета точек кривой Безье
def bezier_curve(points, num=200):
    n = len(points) - 1
    t = np.linspace(0, 1, num)
    curve = np.zeros((num, 3))
    for i in range(n + 1):
        curve += np.outer((1 - t) ** (n - i) * t ** i, points[i]) * binomial_coefficient(n, i)
    return curve

# Биномиальный коэффициент
def binomial_coefficient(n, k):
    return np.math.factorial(n) / (np.math.factorial(k) * np.math.factorial(n - k))

# Получаем точки кривой Безье
bezier_points = bezier_curve(control_points)

# Визуализация кривой Безье и контрольных точек
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(bezier_points[:,0], bezier_points[:,1], bezier_points[:,2], 'r-')
ax.plot(control_points[:,0], control_points[:,1], control_points[:,2], 'bo:')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.title('Кривая Безье')
plt.show()