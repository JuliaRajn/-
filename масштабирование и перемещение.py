import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px
import pandas as pd

# 1. Загрузка примера набора данных (iris)
df = px.data.iris()
df_tips = px.data.tips()

# 2. Пример с диаграммой рассеяния (Scatter plot)
fig1 = go.Figure(data=[go.Scatter(x=df['sepal_length'], y=df['sepal_width'], mode='markers')])

# 3. Настройка панели инструментов для диаграммы рассеяния
fig1.update_layout(
    title='Диаграмма рассеяния (Iris Dataset) с масштабированием и перемещением',
    xaxis_title='Длина чашелистика',
    yaxis_title='Ширина чашелистика',
    dragmode='pan',  # Разрешаем перемещение графика
    hovermode='closest', # Настройка режима наведения
    # Настройка элементов панели инструментов
    modebar_add=['zoom', 'pan', 'zoomIn', 'zoomOut', 'autoScale', 'resetScale'],
)

# 4. Пример со столбчатой диаграммой (Bar chart)
fig2 = go.Figure(data=[go.Bar(x=df_tips['day'], y=df_tips['total_bill'])])

# 5. Настройка панели инструментов для столбчатой диаграммы
fig2.update_layout(
    title='Столбчатая диаграмма (Tips Dataset) с масштабированием и перемещением',
    xaxis_title='День недели',
    yaxis_title='Сумма чека',
    dragmode='pan',  # Разрешаем перемещение графика
    hovermode='x', # Настройка режима наведения
     # Настройка элементов панели инструментов
    modebar_add=['zoom', 'pan', 'zoomIn', 'zoomOut', 'autoScale', 'resetScale'],
)

# 6. Сохранение графиков в HTML
pyo.plot(fig1, filename='диаграмма_рассеяния_с_инструментами.html')
pyo.plot(fig2, filename='столбчатая_диаграмма_с_инструментами.html')
