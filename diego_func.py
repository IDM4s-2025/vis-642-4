from plotly import express as px
import pandas as pd

def diego_func(df:pd.DataFrame):
    fig = px.scatter(df, x="SepalLengthCm", y="PetalLengthCm", color="Species")
    fig.show()