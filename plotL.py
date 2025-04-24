import plotly.express as px

def graficaL():
    df = px.data.iris()
    fig = px.scatter(df, x="petal_width", y="petal_length", color='sepal_length')
    fig.show()

graficaL()