import plotly.express as px

def graficaA(df):
    fig = px.scatter(df, x="PetalLengthCm", y="PetalWidthCm", color="Species",
                 size='SepalWidthCm', hover_data=['SepalLengthCm'])
    fig.show()
