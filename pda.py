from state import State
from transition import Transition

class PDA:
    def __init__(self, q: State):
        self.q = q
        
        self._pilha = ['#']
        self.log = False
        
def makeLog(self):
    self.log = True
    
def run(self, w: str):
    c = w[0] if w else None
    pop = self._pilha[-1]
    
    transitions: set[Transition] = set()
    transitions.update(self.q.transitions(None, None))
    transitions.update(self.q.transitions(c, None))
    transitions.update(self.q.transitions(None, pop))
    transitions.update(self.q.transitions(c, pop))
    
    if self.log:
        print(f'{self.q.name}: {w}')
        print("".join(self._pilha))
        print('-' * 40)
    
    for transition in transitions:
        pda = PDA(transition.state)
        
        pda._pilha = self._pilha.copy()
        pda.log = self.log
        
        if transition.edge.pop:
            pda._pilha.pop()
            
        if transition.edge.push:
            pda._pilha.append(transition.edge.push)

        if pda.run(w[1:] if transition.edge.c else w):
            return True
    
    return c is None and self.q.is_final
