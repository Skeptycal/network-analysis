class HouseCSVParser():
    
    def extract_name(self, col):
        name_chars = []
        for c in col:
            if c == ' ':
                break
            name_chars.append(c)
        return ''.join(name_chars)
    
    def extract_party(self, col):
        for i, c in enumerate(col):
            if c == '(':
                return col[i+1]


    def extract_state(self, col):
        for i, c in enumerate(col):
            if c == '(':
                return col[i+3] + col[i+4]