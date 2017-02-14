import pandas as pd
from graph import Graph

# CSV to dataframe
df = pd.read_csv('data/housedataset.csv')

# Initialize Graph
graph = Graph(df)