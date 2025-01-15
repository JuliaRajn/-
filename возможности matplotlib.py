import matplotlib.pyplot as plt
import pandas as pd

# 1. Загрузка примера данных
data_mpl = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 1, 3, 5]})

# 2. Создание фигуры и осей
fig_mpl, ax_mpl = plt.subplots()

# 3. Установка цвета фона
ax_mpl.set_facecolor('lightblue')

# 4. Создание графика
ax_mpl.plot(data_mpl['x'], data_mpl['y'], marker='o', linestyle='-')

# 5. Настройка заголовка и подписей
ax_mpl.set_title('График Matplotlib с фоном')
ax_mpl.set_xlabel('Ось X')
ax_mpl.set_ylabel('Ось Y')

# 6. Отображение графика
plt.show()
