import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px
import pandas as pd

# 1. Загрузка примера набора данных
df = px.data.tips()

# 2. Создание столбчатой диаграммы
fig = go.Figure(data=[go.Bar(x=df['day'], y=df['total_bill'])])


# 3. Настройка заголовка и подписей осей
fig.update_layout(
    title='Столбчатая диаграмма среднего чека по дням',
    xaxis_title='День недели',
    yaxis_title='Сумма чека'
)

# 4. Сделайте график интерактивным
fig.update_layout(barmode='group', hovermode='x') # задаем режим отображения, hovermode=x - реакция на наведение курсора на столбец

#5. Опубликуйте график
pyo.plot(fig, filename='интерактивный_график_столбчатая.html')

