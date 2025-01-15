import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px
import pandas as pd

# 1. Загрузка примера набора данных (iris)
df = px.data.iris()

# 2. Пример с диаграммой рассеяния (Scatter plot)
fig1 = go.Figure(data=[go.Scatter(x=df['sepal_length'], y=df['sepal_width'], mode='markers')])

# 3. Настройка подписей данных для диаграммы рассеяния
fig1.data[0].hoverinfo = 'text'
fig1.data[0].text = [f"Длина: {sl}, Ширина: {sw}" for sl, sw in zip(df['sepal_length'], df['sepal_width'])]
# создаём текст для каждой точки в формате Длина: значение, Ширина: значение

# 4. Настройка заголовка и подписей осей
fig1.update_layout(
    title='Диаграмма рассеяния (Iris Dataset) с подписями',
    xaxis_title='Длина чашелистика',
    yaxis_title='Ширина чашелистика'
)

# 5.  Пример со столбчатой диаграммой (Bar chart)

df_tips = px.data.tips()

fig2 = go.Figure(data=[go.Bar(x=df_tips['day'], y=df_tips['total_bill'])])

# 6. Настройка подписей для столбчатой диаграммы
fig2.data[0].hoverinfo = 'text'
fig2.data[0].text = [f"Сумма: {tb:.2f}" for tb in df_tips['total_bill']]
#  создаём текст для каждого столбца в формате Сумма: значение с двумя знаками после запятой


# 7. Настройка заголовка и подписей осей
fig2.update_layout(
    title='Столбчатая диаграмма (Tips Dataset) с подписями',
    xaxis_title='День недели',
    yaxis_title='Сумма чека'
)

# 8. Сохранение графиков в HTML

pyo.plot(fig1, filename='диаграмма_рассеяния_с_подписями.html')
pyo.plot(fig2, filename='столбчатая_диаграмма_с_подписями.html')

