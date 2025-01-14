import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.express as px  

# 1. Создание интерактивной диаграммы рассеяния
fig1 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode='markers')])

# Добавьте всплывающую подсказку
fig1.data[0].hoverinfo = 'text'
fig1.data[0].text = ['точка 1', 'точка 2', 'точка 3']

# 2. Создание интерактивной столбчатой диаграммы
fig2 = go.Figure(data=[go.Bar(x=[1, 2, 3], y=[4, 5, 6], text=['4', '5', '6'], textposition='auto')])
# Добавляем текст для вывода на столбцах
# Добавьте всплывающую подсказку
fig2.data[0].hoverinfo = 'y+text'

# 3. Создание интерактивного 3D графика
fig3 = go.Figure(data=[go.Surface(x=[0, 1, 2], y=[0, 1, 2], z=[[4, 6, 8], [5, 7, 9], [6, 8, 10]])])
# 4. Пример с использованием plotly.express
df = px.data.iris()
fig4 = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 hover_data=['petal_width', 'petal_length'])
# 5. Опубликуйте графики в интернете (сохранение в html)
pyo.plot(fig1, filename='интерактивный_график_рассеяния.html')
pyo.plot(fig2, filename='интерактивный_график_столбчатая.html')
pyo.plot(fig3, filename='интерактивный_3d_график.html')
pyo.plot(fig4, filename='интерактивный_график_express.html')

