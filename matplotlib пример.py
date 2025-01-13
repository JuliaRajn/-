# Импортируйте Matplotlib
import matplotlib.pyplot as plt

# Создайте рисунок и оси
fig, ax = plt.subplots()

# Создайте линию
ax.plot([1, 2, 3], [4, 5, 6])

# Настройте внешний вид графика
ax.set_xlabel('X-ось')
ax.set_ylabel('Y-ось')
ax.set_title('Линейный график')

# Сохраните график
plt.savefig('линейный_график.png')

