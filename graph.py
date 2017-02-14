from rowparser import RowParser

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

    def __str__(self):
        return str(self.weight)

    def __repr__(self):
        return str(self.weight)


class Graph():

    def __init__(self, df):
        # place nodes in dictionary data structure
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

    # Construct adjacency matrix graph structure from nodes
    def construct_graph(self):
        # initialize empty adjacency matrix
        self.matrix = [[0 for x in range(len(self.node_dict))] for y in range(len(self.node_dict))]

        # Loop through dict and insert edges into adjacency matrix
        for i in self.node_dict:
            for j in self.node_dict:
                node_a = self.node_dict[i]
                node_b = self.node_dict[j]
                # Calculate edge weight between nodes a and b
                tie_strength = node_a.calculate_tie_strength(node_b)
                # Insert edge into graph
                self.matrix[node_a.key][node_b.key] = Edge(tie_strength)