import numpy as np
class HouseCSVParser():
    
    # Return Surname of representative as string
    def extract_name(self, col):
        name_chars = []
        for c in col:
            if c == ' ':
                break
            name_chars.append(c)
        return ''.join(name_chars)
    
    # Return party of representative as string ('D', 'R')
    def extract_party(self, col):
        for i, c in enumerate(col):
            if c == '(':
                return col[i+1]

    # Return State (i.e NY) of representative as string
    def extract_state(self, col):
        for i, c in enumerate(col):
            if c == '(':
                return col[i+3] + col[i+4]
    
    # Return set of Votes in which representative voted given value
    def get_votes(self, row, value):
        votes = { i - 1 for i, v in enumerate(row) if i > 1 and not np.isnan(v) and int(v) == value}
        return votes
        
        
