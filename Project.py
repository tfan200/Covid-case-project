import pandas as pd
import plotly.express as px

from DataFrame import Df
DaFr = pd.read_csv("csv files/Proj.csv")
fig3 = px.scatter(DaFr,x = "date", y = "cases", color = "country",title = "Covid Cases")
fig3.show()