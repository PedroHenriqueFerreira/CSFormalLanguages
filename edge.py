class Edge:
    def __init__(self, c: str, pop: str, push: str):
        self.c = c
        self.pop = pop
        self.push = push
        
    def __eq__(self, e: 'Edge'):
        if not isinstance(e, Edge):
            return False
    
        return self.c == e.c and self.push == e.push and self.pop == e.pop
    
    def __hash__(self):
        return hash((self.c, self.push, self.pop))
    
    def __repr__(self):
        return f'edge[{self.c}, {self.pop}, {self.push}]'
