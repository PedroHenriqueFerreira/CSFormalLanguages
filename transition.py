from typing import TYPE_CHECKING

from edge import Edge

if TYPE_CHECKING:
    from state import State

class Transition:
    def __init__(self, state: 'State', edge: Edge):
        self.state = state
        self.edge = edge
        
    def __eq__(self, t: 'Transition'):
        if not isinstance(t, Transition):
            return False
    
        return self.state == t.state and self.edge == t.edge
    
    def __hash__(self):
        return hash((self.state, self.edge))
    
    def __repr__(self):
        return f'{self.edge} -> {self.state}'