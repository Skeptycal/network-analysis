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
    def __init__(self, weight):
        self.weight = weight

class Graph():
    def __init__(self, df):
        # place nodes in dictionary data structure
        self.node_dict = self.generate_dictionary(df) 
        self.construct_graph()
        print(self.matrix)
    
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
            node_dict[int(node.key)] = node

        return node_dict

    def construct_graph(self):
        # initialize empty adjacency matrix
        self.matrix = [[0 for x in range(len(self.node_dict))] for y in range(len(self.node_dict))]
        
        # Loop through dict and insert edges into adjacency matrix
        for i in self.node_dict:
            for j in self.node_dict:
                a = self.node_dict[i]
                b = self.node_dict[j]
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


