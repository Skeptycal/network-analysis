import pandas as pd

class Node():
    def __init__(self, num, name, party, state, region):
        self.num = num
        self.name = name
        self.party = party
        self.state = state
        self.region = region
        self.yvotes = set()
        self.nvotes = set()
    
    def add_vote(self, num, decision):
        if(decision == 1):
            self.yvotes.add(num)
        elif(decision == 0):
            self.nvotes.add(num)
    
    def calcluate_tie_strength(self, node):
        # count positive strength (same votes)

        # subtract negative strength (differing votes)

        # return result
        return 0

class Edge():
    def __init__(self):
        self.weight = 0

class Graph():
    def __init__(self, node_list):
        # place nodes in dictionary data structure
        self.node_dict = generate_dictionary(node_list) 
        self.construct_graph()
    
    def generate_dictionary(self, node_list):
        pass

    def construct_graph(self, node_list):
        pass

    def print_nodes(self):
        pass
    
    def print_edges(self):
        pass
    
    def print_node_info(self):
        pass
    
class HouseCSVParser():
    
    def extract_name(self, row):
        pass
    
    def extract_party(self, row):
        pass

    def extract_state(self, row):
        pass


df = pd.read_csv('housedataset.csv')


for row in df.itertuples():
    print(row)





