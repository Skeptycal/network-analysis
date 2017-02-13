import pandas as pd
from housecsvparse import HouseCSVParser

class Node():
    def __init__(self, key, name, party, state, yes_votes, no_votes):
        self.key = key
        self.name = name
        self.party = party
        self.state = state
        # self.region = region may investigate later
        self.yes_votes = yes_votes
        self.no_votes = no_votes
    
    
    
    def calcluate_tie_strength(self, node):
        # count positive strength (same votes)

        # subtract negative strength (differing votes)

        # return result
        return 0

class Edge():
    def __init__(self, weight):
        self.weight = weight

class Graph():
    def __init__(self, df):
        # place nodes in dictionary data structure
        self.node_dict = self.generate_dictionary(df) 
        #self.construct_graph()
    
    def generate_dictionary(self, node_list):
        # Create parser object
        h = HouseCSVParser()
        # For each row, create node object and insert into dict
        node_dict = {}
        for row in df.itertuples():
            # Create node 
            name = h.extract_name(row[1])
            party = h.extract_party(row[1])
            state = h.extract_state(row[1])
            yes_votes = h.get_votes(row, 1)
            no_votes = h.get_votes(row, 0)
            node = Node(row[0], name, party, state, yes_votes, no_votes)
            # Insert node into dict
            node_dict[node.key] = node

        return node_dict

    def construct_graph(self):
        # initialize empty adjacency matrix
        self.matrix = [[0 for x in range(len(dict))] for y in range(len(dict))]
        for a in self.node_dict:
            for b in self.node_dict:
                self.matrix[a.key][b.key] = Edge(a.calculate_tie_strength(b))
        
    def print_nodes(self):
        pass
    
    def print_edges(self):
        pass
    
    def print_node_info(self):
        pass
    

# CSV to dataframe
df = pd.read_csv('housedataset.csv')

# Initialize Graph
g = Graph(df)


