import pandas as pd
from graph import Graph

# CSV to dataframe
df = pd.read_csv('data/113senate.csv')

# Initialize Graph
g = Graph(df)


# Samples
m = g.matrix
n = g.node_dict
print(n[37], n[89], '\n', m[37][89])

print(n[100], n[89], '\n', m[100][89])

print(n[12], n[21], '\n', m[12][21])

print(n[100], n[21], '\n', m[100][21])