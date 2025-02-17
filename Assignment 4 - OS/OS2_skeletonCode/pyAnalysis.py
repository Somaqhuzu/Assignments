import pandas as pd
import scipy.stats as sci
import numpy as np
import matplotlib.pyplot as pt

def histogram(frame,column):
    import plotly.graph_objects as go
    
    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x = frame[frame["Algorithm"]=="FCFS"][column],
        histfunc="count",
        xbins=dict(start=0,end=200000,size=10000),
        name="FCFS",
        texttemplate="%{x},  %{y}",
    ))
    fig.add_trace(go.Histogram(
        x=(frame[frame["Algorithm"]=="SJF"][column]),
        name="SJF",
        histfunc="count",
        xbins=dict(start=0,end=200000,size=10000),
        texttemplate="%{x},  %{y}",
 
    ))
    fig.update_layout(
        title_text = "{col} for each Algorithm".format(col=column),
        xaxis_title_text="{col} Range".format(col=column),
        yaxis_title_text = "Number of Patrons",
        bargroupgap= 0.0,
        bargap=0.2
        )
    fig.show()
    print("FCFS Average value({column}):{avg}".format(avg=frame[frame["Algorithm"]=="FCFS"][column].agg("mean"),column=column))
    print("SJF Average value({column}):{avg}".format(avg=frame[frame["Algorithm"]=="SJF"][column].agg("mean"),column=column))
    
if __name__=='__main__':
    data = pd.read_csv("data.txt")
    print(data)
    metrics = ["Turn Around Time","Waiting Time","Response Time"]
    for metric in metrics:
        histogram(data,metric)
    