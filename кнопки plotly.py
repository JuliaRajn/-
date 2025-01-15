import plotly.graph_objects as go
# Пример данных для графика
x = [1, 2, 3, 4]
y1 = [10, 11, 12, 13]
y2 = [15, 16, 17, 18]
y3 = [20, 21, 22, 23]
y4 = [25, 26, 27, 28] # Добавим 4-ый трейс
# Создаем фигуры
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y1, name='Трейс 1'))
fig.add_trace(go.Scatter(x=x, y=y2, name='Трейс 2'))
fig.add_trace(go.Scatter(x=x, y=y3, name='Трейс 3'))
fig.add_trace(go.Scatter(x=x, y=y4, name='Трейс 4')) # Добавим 4-ый трейс
# Создаем кнопки
fig.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(
                    label='Показать все',
                    method='update',
                    args=[{'visible': [True]*len(fig.data)}] # исправлено, передаем видимость для всех трейсов
                ),
                dict(
                    label='Скрыть все',
                    method='update',
                    args=[{'visible': [False]*len(fig.data)}] # создадим кнопку для скрытия всех трейсов
                )
            ]
        )
    ]
)

fig.show()


