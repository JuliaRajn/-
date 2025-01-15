import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Загрузка примера набора данных
df = sns.load_dataset('iris')  

# 2. Установка стиля графика
sns.set_style('whitegrid')

# 3. Используйте цветовую палитру
sns.set_palette('muted')

# 4. Создание гистограммы
plt.figure(figsize=(8,6))
sns.histplot(data=df, x='sepal_length', kde=True, color='skyblue') # использую 'sepal_length' из iris data
plt.title('Гистограмма длин чашелистиков (Iris Dataset)')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75) # Добавим сетку по оси y
plt.show()




