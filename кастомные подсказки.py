import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px
import pandas as pd

# 1. Загрузка примера набора данных (iris)
df = px.data.iris()
df_tips = px.data.tips()

# 2. Пример с диаграммой рассеяния (Scatter plot)
fig1 = go.Figure(data=[go.Scatter(x=df['sepal_length'], y=df['sepal_width'], mode='markers')])

# 3. Настройка внешнего вида всплывающих подсказок для диаграммы рассеяния
fig1.data[0].hovertemplate = (
    "<b>Длина чашелистика:</b> %{x}<br>"
    "<b>Ширина чашелистика:</b> %{y}<br>"
    "<extra>Дополнительная информация</extra>"
)
# <extra> отключает стандартную дополнительную информацию от Plotly

# 4. Настройка заголовка и подписей осей
fig1.update_layout(
    title='Диаграмма рассеяния (Iris Dataset) с кастомными всплывающими подсказками',
    xaxis_title='Длина чашелистика',
    yaxis_title='Ширина чашелистика'
)

# 5. Пример со столбчатой диаграммой (Bar chart)
fig2 = go.Figure(data=[go.Bar(x=df_tips['day'], y=df_tips['total_bill'])])

# 6. Настройка внешнего вида всплывающих подсказок для столбчатой диаграммы
fig2.data[0].hovertemplate = (
    "<b>День недели:</b> %{x}<br>"
    "<b>Сумма чека:</b> %{y:.2f} <br>"
    "<extra>Дополнительная информация</extra>"
)
# Используем .2f чтобы ограничить вывод 2 знаками после запятой

# 7. Настройка заголовка и подписей осей
fig2.update_layout(
    title='Столбчатая диаграмма (Tips Dataset) с кастомными всплывающими подсказками',
    xaxis_title='День недели',
    yaxis_title='Сумма чека'
)


# 8. Сохранение графиков в HTML

pyo.plot(fig1, filename='диаграмма_рассеяния_с_кастомными_подсказками.html')
pyo.plot(fig2, filename='столбчатая_диаграмма_с_кастомными_подсказками.html')
