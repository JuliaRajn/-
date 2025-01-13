import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 1. Загрузка примера набора данных
df = sns.load_dataset('tips')

# 2. Создайте boxplot
plt.figure(figsize=(10, 6)) # устанавливаем размер графика
sns.boxplot(data=df, x='day', y='total_bill', palette='Set2')
plt.title('Boxplot распределения общего счета по дням')
plt.xlabel('День недели')
plt.ylabel('Общий счет')
plt.grid(axis='y', alpha=0.75) # добавляем сетку по оси y
plt.show()



