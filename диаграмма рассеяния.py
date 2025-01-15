import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px
import pandas as pd

# 1. Загрузка примера набора данных
df = px.data.iris()

# 2. Создайте диаграмму рассеяния
fig = go.Figure(data=[go.Scatter(x=df['sepal_length'], y=df['sepal_width'], mode='markers')]) # mode='markers' чтобы отображались точки

# 3. Настройка заголовка, подписей осей
fig.update_layout(
    title='Диаграмма рассеяния (Iris Dataset)',
    xaxis_title='Длина чашелистика',
    yaxis_title='Ширина чашелистика'
)


# 4. Сделайте график интерактивным
fig.update_layout(hovermode='closest') # задает реакцию на наведение курсора

#5. Опубликуйте график
pyo.plot(fig, filename='интерактивный_график_рассеяния.html')


