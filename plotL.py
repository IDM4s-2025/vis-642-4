import plotly.express as px

def graficaL(df):
    fig = px.scatter(df, x="PetalWidthCm", y="PetalLengthCm", color='SepalLengthCm')
    fig.show()
