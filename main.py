import pandas as pd
from graph import Graph

# CSV to dataframe
df = pd.read_csv('data/109houseofrep.csv')

# Initialize Graph
graph = Graph(df)