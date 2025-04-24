import plotly.express as px

def graficaA():
    df = px.data.iris()
    fig = px.scatter(df, x="petal_length", y="petal_width", color="species",
                 size='sepal_width', hover_data=['sepal_length'])
    fig.show()

graficaA()