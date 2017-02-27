from rowparser import RowParser
import math

class Node():

    def __init__(self, key, name, party, state, yes_votes, no_votes):
        self.key = key
        self.name = name
        self.party = party
        self.state = state
        # self.region = region may investigate later
        self.yes_votes = yes_votes
        self.no_votes = no_votes
    
    def __repr__(self):
        return self.name + ", " + self.party + ", " + self.state

    def calculate_tie_strength(self, node):
        tie_strength = 0
        # count positive strength (same votes)
        # Count Yes votes in common
        tie_strength += len(self.yes_votes.intersection(node.yes_votes))
        # Count No votes in common
        tie_strength += len(self.no_votes.intersection(node.no_votes))

        # subtract negative strength (differing votes)
        # Count when A voted Yes and B voted no
        tie_strength -= len(self.yes_votes.intersection(node.no_votes))
        # Count when A voted No and B voted yes
        tie_strength -= len(self.no_votes.intersection(node.yes_votes))

        return tie_strength


class Edge():

    # Weight calculated via node, party = True if 2 nodes are in same party,
    #  state = True if 2 nodes are same state
    def __init__(self, weight, party, state):
        self.weight = weight
        self.party = party
        self.state = state

    def __repr__(self):
        return str(self.weight) + ", " +  str(self.party) + ", " + str(self.state)


# Graph constructor is called with a data frame object, to get node information.
# To recreate the data structure with different edge parameters, call construct_graph. 
# By default, a graph including all edges is created upon object construction.
# Graph is stored as both an adjacency list and adjacency matrix structure.
# Note: Adjacency list structure will not contain tie strength and other information.
class Graph():

    def __init__(self, df):
        self.matrix = None
        self.adj_list = None
        self.node_dict = self.generate_dictionary(df)
        self.construct_graph()

    # Read dataframe into node objects
    def generate_dictionary(self, df):
        # Create parser object
        rp = RowParser()
        # For each row, create node object and insert into dict
        node_dict = {}
        for row in df.itertuples():
            # Create node
            name = rp.extract_name(row[1])
            party = rp.extract_party(row[1])
            state = rp.extract_state(row[1])
            yes_votes = rp.get_votes(row, 1)
            no_votes = rp.get_votes(row, 0)
            node = Node(row[0], name, party, state, yes_votes, no_votes)
            # Insert node into dict
            node_dict[int(node.key)] = node

        return node_dict

    # Construct graph data structures (Adjacency Matrix and Adjacency List)
    # positive: If set to True, only insert positive tie strengths as edges.
    # min_strength: If provided, only insert edges with at least this tie strength.
    def construct_graph(self, positive=False, min_strength=0):

        # Initialize empty adjacency matrix.
        self.matrix = [[0 for x in range(len(self.node_dict))] for y in range(len(self.node_dict))]

        # Initialize empty adjacency list.
        self.adj_list = [list() for x in range(len(self.node_dict))]

        # Loop through dict and insert edges into data structures.
        for i in self.node_dict:
            for j in self.node_dict:
                node_a = self.node_dict[i]
                node_b = self.node_dict[j]

                # Do not insert a self-loop edge
                if node_a.key != node_b.key:
                    # Calculate edge weight between nodes a and b
                    tie_strength = node_a.calculate_tie_strength(node_b)
                    party = node_a.party == node_b.party
                    state = node_a.state == node_b.state

                    # Create Edge
                    edge = Edge(tie_strength, party, state)

                    # Insert edge into graph if conditions are met:
                    insert = False
                    if not positive and math.fabs(edge.weight) >= min_strength:
                        insert = True
                    if positive and edge.weight >= min_strength:
                        insert = True
                    if insert:
                        # Insert into matrix[i][j] and matrix [j][i]
                        self.matrix[node_a.key][node_b.key] = edge
                        self.matrix[node_b.key][node_a.key] = edge

                        # Append to adjacency list[i]
                        self.adj_list[node_a.key].append(node_b.key)
            


                