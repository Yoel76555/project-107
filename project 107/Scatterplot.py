import pandas as pd
import plotly.express as px
import csv

df= pd.read_csv("data.csv")
mean= df.groupby(["students_id","level"],as_index=False)["attempt"].mean()

fig = px.scatter(mean, x="students_id", y="level", 
                   size="attempt", color="attempt")
fig.show()
