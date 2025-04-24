from plotly import express as px
import pandas as pd

def diego_func(df:pd.DataFrame):
    fig = px.scatter(df, x="SepalWidthCm", y="SepalLengthCm", color="Species")
    fig.show()