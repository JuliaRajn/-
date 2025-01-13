import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Загрузка примера набора данных
data = sns.load_dataset('iris')  # Используем набор данных 'iris'

# 1. Создание гистограммы
plt.figure(figsize=(8, 6))  # Установка размера графика
sns.histplot(data=data, x='sepal_length', kde=True, color='skyblue') # kde=True добавляет линию плотности распределения
plt.title('Гистограмма длин чашелистиков (Iris Dataset)')
plt.xlabel('Длина чашелистика (см)')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.75) # Добавим сетку по оси y
plt.show()

# 2. Создание тепловой карты корреляций
numeric_data = data.select_dtypes(include=['number']) # выбираем только числовые данные для построения тепловой карты
correlation_matrix = numeric_data.corr() # вычисляем корреляционную матрицу

plt.figure(figsize=(8, 6)) # устанавливаем размер графика
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5) # annot=True выводит значения корреляций, cmap задаёт цветовую схему, linewidths - ширина линий между ячейками
plt.title('Тепловая карта корреляций (Iris Dataset)')
plt.show()

# 3. Пример тепловой карты на другом примере
data_flights = sns.load_dataset('flights')
flights_pivot = data_flights.pivot(index='month', columns='year', values='passengers')

plt.figure(figsize=(10, 8))
sns.heatmap(flights_pivot, cmap='viridis', annot=True, fmt="d", linewidths=.5)
plt.title('Тепловая карта пассажирских перевозок')
plt.xlabel('Год')
plt.ylabel('Месяц')
plt.show()

