import pandas as pd
from graph import Graph
from measures import neighborhood_overlap, degree_distribution, clustering_coefficient, neighborhood_overlap_csv, plot_degree_distribution

# CSV to dataframe
df = pd.read_csv('data/113senate.csv')

# Initialize Graph
graph = Graph(df)
graph.construct_graph(True, 0)

g = graph.adj_list

# Compute neighborhood overlap of each edge.
overlap = neighborhood_overlap(g)
# Write neighborhood overlap to a CSV file.
neighborhood_overlap_csv(overlap)

# Compute and plot degree distribution of the graph.
d = degree_distribution(g)
plot_degree_distribution(d)

# Compute clustering coefficient.
clustering = clustering_coefficient(g)
print(clustering)
