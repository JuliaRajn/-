import plotly.graph_objects as go
import plotly.offline as pyo
import pandas as pd

# 1. Загрузка примера данных
data_plotly = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 1, 3, 5]})


# 2. Создание фигуры
fig_plotly = go.Figure()

# 3. Добавление графика
fig_plotly.add_trace(go.Scatter(x=data_plotly['x'], y=data_plotly['y'], mode='markers+lines'))

# 4. Настройка цвета фона
fig_plotly.update_layout(
    plot_bgcolor='lightblue',
    paper_bgcolor='lavender',
    title='График Plotly с фоном',
    xaxis_title='Ось X',
    yaxis_title='Ось Y'
)

# 5. Сохранение графика в HTML
pyo.plot(fig_plotly, filename='plotly_background.html')

