import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Загрузка примера данных
data_sns = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 1, 3, 5]})

# 2. Установка темы и цвета фона
sns.set_theme(style='whitegrid', palette='pastel')
sns.set(rc={"axes.facecolor": "lavender", "figure.facecolor": "lavender"})

# 3. Создание графика
plt.figure(figsize=(8,6))
sns.lineplot(data=data_sns, x='x', y='y', marker='o')
plt.title('График Seaborn с фоном')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')

# 4. Отображение графика
plt.show()
