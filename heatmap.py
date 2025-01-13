import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Загрузка примера набора данных
df = sns.load_dataset('iris')

# 2. Выбор числовых столбцов
numeric_df = df.select_dtypes(include=['number'])

# 3. Вычисление корреляционной матрицы
correlation_matrix = numeric_df.corr()

# 4. Создание heatmap
plt.figure(figsize=(8, 6)) # устанавливаем размер графика
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5) #  добавляем подписи, цветовую палитру и линии между ячейками
plt.title('Тепловая карта корреляций (Iris Dataset)') # задаем заголовок
plt.show()




