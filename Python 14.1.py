import numpy as np
import matplotlib.pyplot as plt

# Визначення функції
def Y(x):
    return 10 * np.cos(x**2) / x**2

# Генерація значень x в інтервалі [0, 5] з кроком 0.1
x = np.arange(0.1, 5.1, 0.1)

# Обчислення відповідних значень y
y = Y(x)

# Побудова графіка
plt.plot(x, y, linestyle='-', color='green', linewidth=2, label='Y(x) = 10*cos(x^2)/x^2')

# Позначення осей
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Додавання заголовка та підписів осей
plt.title('Графік функції Y(x)')
plt.xlabel('x')
plt.ylabel('Y(x)')

# Додавання легенди
plt.legend()

# Відображення графіка
plt.show()