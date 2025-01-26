from edge import Edge
from transition import Transition

class State:
    def __init__(self, name: str):
        self.name = name
        
        self.is_final = False
        self._transitions: list[Transition] = []
        
    def setFinal(self):
        self.is_final = True
        
    def addTransition(self, state: 'State', c: str, pop: str, push: str):
        return self.addTransitions(state, Edge(c, pop, push))

    def addTransitions(self, state: 'State', *edges: Edge):
        for edge in edges:
            transition = Transition(state, edge)
            
            if transition in self._transitions:
                continue
            
            self._transitions.append(transition)
            
        return self
    
    def transitions(self, c: str, pop: str):
        transitions: set[Transition] = set()
        
        for transition in self._transitions:
            if c == transition.edge.c and pop == transition.edge.pop:
                transitions.add(transition)
                
        return transitions
    
    def __eq__(self, s: 'State'):
        if not isinstance(s, State):
            return False
    
        return self.name == s.name
    
    def __hash__(self):
        return hash((self.name, ))
    
    def __repr__(self):
        return self.name