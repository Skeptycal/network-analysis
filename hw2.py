# CSE 392 HW 2 Tasks
# Compute the following values: neighborhood overlap, degree distribution, clustering coefficient

from math import factorial
import csv
import matplotlib.pyplot as plt

# Compute the overlap of neighborhood for each edge uv
# For each edge, compute the neighborhood overlap.abs
# g = graph structure
def neighborhood_overlap(g):
    # Tuples in format of (vertex v, vertex u, neighborhood overlap)
    overlap = []
    # Avoid counting the same edge twice. Set of Tuples (u,v).
    visited = set()
    for i in range(len(g)):
        for j in g[i]:
            u = i
            v = j
            # Check if edge visited
            if (u, v) in visited or (v, u) in visited:
                pass
            else:
                # Mark as visited
                visited.add((u, v))
                # Get set of neighbors of u
                u_neighbors = set()
                for x in g[u]:
                    u_neighbors.add(x)
                # Get set of neighbors of v
                v_neighbors = set()
                for x in g[v]:
                    v_neighbors.add(x)
                # Get the intersection of N(u) and N(v)
                intersection = u_neighbors.intersection(v_neighbors)
                # Get the union of N(u) and N(v)
                union = u_neighbors.union(v_neighbors)
                # Get the overlap |N(u) intersect N(v)| / |N(u) union N(v)|
                overlap_uv = len(intersection) / len(union)
                # Append to output list
                overlap.append((u, v, overlap_uv))
    return overlap

def neighborhood_overlap_csv(overlap):
    with open("neighborhood_overlaps.csv", "w") as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['u', 'v', 'Overlap'])
        for row in overlap:
            csv_out.writerow(row)

# Compute the degree distribution of the graph, as the percentage of nodes with degree k for each value of k.
def degree_distribution(g):
    # Get node with highest degree:
    max_k = max(len(x) for x in g)
    distribution = [0 for x in range(max_k+1)]

    # Count nodes with each degree k
    for x in g:
        distribution[len(x)] += 1

    # Get percentage of nodes with degree k for each value of k
    distribution = [x/len(g) for x in distribution]
    return distribution

# Plot the degree distribution of the graph
def plot_degree_distribution(d):
    d = [x * 100 for x in d]
    plt.plot(range(len(d)), d, 'ro')
    plt.ylabel("Percentage")
    plt.xlabel("Degree")
    plt.show()


# Compute the clustering coefficient of the graph
def clustering_coefficient(g):
    # Find number of triangles, which are cycles of length 3.abs
    # Keep track of counted triangles, where each element of the set is (x, y, z),
    #  where x, y and z are in ascending order.
    triangles = set()

    # For each edge (i,j)
    for i in range(len(g)):
        for j in g[i]:
            # Check if (j,k) and (k,i) is an edge, where k is connected to j.
            for k in g[j]:
                if k in g[i]:
                    triangle = [i, j, k]
                    triangle.sort()
                    triangles.add(tuple(triangle))

    num_triangles = len(triangles)

    # return number of triangles / n c 3
    return num_triangles / combination(len(g), 3)

def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))


