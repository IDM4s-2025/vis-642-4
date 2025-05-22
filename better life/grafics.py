from matplotlib import pyplot as plt 
from plotly import express as px ,graph_objects as go
import pandas as pd
import numpy as np
import seaborn as sns 

traductor = {}

def load_data(path:str)->pd.DataFrame:
    data = pd.read_csv(path)
    global traductor
    traductor  = {"LOCATION":{},"INDICATOR":{}}
    countrys = list(pd.unique(data["LOCATION"]))


    table_dict = {} 


    for indic in list(pd.unique(data["INEQUALITY"])):
        table_dict[indic] = {}
        for locat in countrys:
            table_dict[indic].update({locat:{}})

    for i,row in data.iterrows():
        if not(row["INDICATOR"] in traductor["INDICATOR"].keys()):
            traductor["INDICATOR"][row["INDICATOR"]] = row["Indicator"]
        
        if not(row["LOCATION"] in traductor["LOCATION"].keys()):
            traductor["LOCATION"][row["LOCATION"]] = row["Country"]
        table_dict[row["INEQUALITY"]][row["LOCATION"]].update({row["INDICATOR"]:row["OBS_VALUE"]})

    table = pd.DataFrame()

    for indic in list(pd.unique(data["INEQUALITY"])):
        for locat in countrys:
            temp = pd.Series(table_dict[indic][locat])
            temp["LOCATION"] = locat
            temp["INEQUALITY"] = indic
            table = pd.concat([table,temp.copy().to_frame().T])

    return table


def polinomic_fit(x_data:pd.Series,y_data:pd.Series,degree:int = 0):
    temp = x_data.to_frame()
    temp[y_data.name] = y_data
    temp = temp.dropna()
    temp = temp.astype(np.float64)
    coeficients = np.polyfit(temp[x_data.name],temp[y_data.name],degree)
    fit = np.poly1d(coeficients)
    return list(fit(x_data))

def ploly_sactter(data:pd.DataFrame,xlable:str,ylable:str,titulo:str = "",inecual:str = "TOT",trend:int = 0):
    data_plt = data[data["INEQUALITY"] == inecual]
    #data_plt = data
    locations = data_plt["LOCATION"].map(traductor["LOCATION"])
    if (titulo == ""):
        titulo = traductor["INDICATOR"][xlable]+ " contra "+traductor["INDICATOR"][ylable]
    fig = px.scatter(data_plt,x=xlable,y=ylable,hover_name=locations,title=titulo)
    fig.update_layout(xaxis_title=traductor["INDICATOR"][xlable],yaxis_title=traductor["INDICATOR"][ylable])
    if(trend > 0):
        z = polinomic_fit(data_plt[xlable],data_plt[ylable],trend)
        fig.add_trace(go.Scatter(x=data_plt[xlable],y=z,mode='lines'))

    fig.show()

def plotly_line(data:pd.DataFrame,xlable:str,ylable:str,titulo:str = "",inecual:str = "TOT"):
    #data_plt = data[data["INEQUALITY"] == inecual]
    data_plt = data
    locations = data_plt["LOCATION"].map(traductor["LOCATION"])
    if (titulo == ""):
        titulo = traductor["INDICATOR"][xlable]+ " contra "+traductor["INDICATOR"][ylable]
    fig = px.plot(data_plt,x=xlable,y=ylable,hover_name=locations,title=titulo)
    fig.update_layout(xaxis_title=traductor["INDICATOR"][xlable],yaxis_title=traductor["INDICATOR"][ylable])
    fig.show()

def get_corelation(data:pd.DataFrame,graph_dimentions:tuple[float,float]=(None,None),inecual:str = "TOT",col:list = ["LOCATION","INEQUALITY"]):
    if (graph_dimentions != (None,None)):
       plt.figure(figsize=graph_dimentions)
    else:
        plt.figure()

    plt.title('CORRELATION MATRIX', fontweight='bold') 
    #data_plt = data[data["INEQUALITY"] == inecual]
    data_plt = data
    sns.heatmap(data_plt.drop(columns=col).corr(), annot=True)
    
    plt.show()