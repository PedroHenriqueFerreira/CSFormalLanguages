from state import State
from utils import Utils
from pda import PDA

from time import time

class Instances:
    @staticmethod
    def fromGrammar(file_name: str, w: str, log = False):
        # Lendo arquivo
        
        grammar = Utils.readFile(file_name)
    
        start = ''
    
        rules: list[tuple[str, str]] = []
        esq: set[str] = set()
        dir: set[str] = set()
        
        for rule in grammar.split('\n'):
            e, d = rule.split('->')
            e, d = e.strip(), d.strip()
            
            if len(e) != 1:
                raise Exception('Gramática inválida')

            if not start:
                start = e

            for i in d.split('|'):
                dd = i.strip()
                
                if not dd:
                    continue
                
                rules.append((e, dd))
                esq.add(e)
                dir.update(c for c in dd if c != 'λ')
        
        dir = dir - esq
        
        # Criando PDA
        
        q0 = State('q0')
        q1 = State('q1')
        q2 = State('q2')
        qf = State('qf')
        
        qf.setFinal()
        
        q0.addTransition(q1, None, None, '$')
        q1.addTransition(q2, None, None, start)
        
        counter = 3
        
        for rule in rules:
            if rule[1] == 'λ':
                q2.addTransition(q2, None, rule[0], None)
                continue
            
            state = q2
            
            if len(rule[1]) > 1:
                state = State(f'q{counter}')
                counter += 1
            
            q2.addTransition(state, None, rule[0], rule[1][-1])
            
            for c in rule[1][1:-1][::-1]:
                new_state = State(f'q{counter}')
                counter += 1
                
                state.addTransition(new_state, None, None, c)
                
                state = new_state
            
            if len(rule[1]) > 1:
                state.addTransition(q2, None, None, rule[1][0])
    
        for d in dir:
            q2.addTransition(q2, d, d, None)
   
        q2.addTransition(qf, None, '$', None)
        
        pda = PDA(q0)
        
        if log:
            pda.makeLog()
        
        elapsed = time()
        
        Utils.checkout(pda.run(w),w)
        
        elapsed = time() - elapsed
        
        print(f'Tempo gasto: {elapsed:.3f}s')
    
    @staticmethod
    def enquanto(w: str):
        # S -> λ
        # S -> eqt(a){S}S
    
        q0 = State('q0')
        q1 = State('q1')
        q2 = State('q2')
        qf = State('qf')
        
        qa = State('qa')
        qb = State('qb')
        qc = State('qc')
        qd = State('qd')
        qe = State('qe')
        qg = State('qg')
        qh = State('qh')
        qi = State('qi')
        qj = State('qj')
    
        qf.setFinal()
        
        q0.addTransition(q1, None, None, '$')
        q1.addTransition(q2, None, None, 'S')
    
        # S -> eqt(a){S}S
        q2.addTransition(qa, None, 'S', 'S')
        qa.addTransition(qb, None, None, '}')
        qb.addTransition(qc, None, None, 'S')
        qc.addTransition(qd, None, None, '{')
        qd.addTransition(qe, None, None, ')')
        qe.addTransition(qg, None, None, 'a')
        qg.addTransition(qh, None, None, '(')
        qh.addTransition(qi, None, None, 't')
        qi.addTransition(qj, None, None, 'q')
        qj.addTransition(q2, None, None, 'e')
        
        # S -> λ
        q2.addTransition(q2, None, 'S', None)
        
        q2.addTransition(q2, 'e', 'e', None)
        q2.addTransition(q2, 'q', 'q', None)
        q2.addTransition(q2, 't', 't', None)
        q2.addTransition(q2, '(', '(', None)
        q2.addTransition(q2, 'a', 'a', None)
        q2.addTransition(q2, ')', ')', None)
        q2.addTransition(q2, '{', '{', None)
        q2.addTransition(q2, '}', '}', None)
        
        q2.addTransition(qf, None, '$', None)
        
        pda = PDA(q0)
        
        elapsed = time()
        
        Utils.checkout(pda.run(w),w)
        
        elapsed = time() - elapsed
        
        print(f'Tempo gasto: {elapsed:.3f}s')
         
    staticmethod
    def se(w: str):
        # S -> se(a){S}TUS
        # S -> λ   
        # T -> senaose(a){S}T
        # T -> λ
        # U -> senao{S}
        # U -> λ
        
        q0 = State('q0')
        q1 = State('q1')
        q2 = State('q2')
        qf = State('qf')
        
        qa = State('qa')
        qb = State('qb')
        qc = State('qc')
        qd = State('qd')
        qe = State('qe')
        qg = State('qg')
        qh = State('qh')
        qi = State('qi')
        qj = State('qj')
        qk = State('qk')
        ql = State('ql')
        qm = State('qm')
        qn = State('qn')
        qo = State('qo')
        qp = State('qp')
        qq = State('qq')
        qr = State('qr')
        qs = State('qs')
        qt = State('qt')
        qu = State('qu')
        qv = State('qv')
        qw = State('qw')
        qx = State('qx')
        qy = State('qy')
        
        qaa = State('qaa')
        qbb = State('qbb')
        qcc = State('qcc')
        qdd = State('qdd')
        qee = State('qee')
        qff = State('qff')
        qgg = State('qgg')
        
        qf.setFinal()
        
        q0.addTransition(q1, None, None, '$')
        q1.addTransition(q2, None, None, 'S')
        
        # S -> se(a){S}TUS
        q2.addTransition(qa, None, 'S', 'S')
        qa.addTransition(qb, None, None, 'U')
        qb.addTransition(qc, None, None, 'T')
        qc.addTransition(qd, None, None, '}')
        qd.addTransition(qe, None, None, 'S')
        qe.addTransition(qg, None, None, '{')
        qg.addTransition(qh, None, None, ')')
        qh.addTransition(qi, None, None, 'a')
        qi.addTransition(qj, None, None, '(')
        qj.addTransition(qk, None, None, 'e')
        qk.addTransition(q2, None, None, 's')
        
        # S -> λ
        q2.addTransition(q2, None, 'S', None)
        
        # T -> senaose(a){S}T
        q2.addTransition(qm, None, 'T', 'T')
        qm.addTransition(qn, None, None, '}')
        qn.addTransition(qo, None, None, 'S')
        qo.addTransition(qp, None, None, '{')
        qp.addTransition(qq, None, None, ')')
        qq.addTransition(qr, None, None, 'a')
        qr.addTransition(qs, None, None, '(')
        qs.addTransition(qt, None, None, 'e')
        qt.addTransition(qu, None, None, 's')
        qu.addTransition(qv, None, None, 'o')
        qv.addTransition(qw, None, None, 'a')
        qw.addTransition(qx, None, None, 'n')
        qx.addTransition(qy, None, None, 'e')
        qy.addTransition(q2, None, None, 's')
        
        # T -> λ
        q2.addTransition(q2, None, 'T', None)
        
        # U -> senao{S}
        q2.addTransition(qaa, None, 'U', '}')
        qaa.addTransition(qbb, None, None, 'S')
        qbb.addTransition(qcc, None, None, '{')
        qcc.addTransition(qdd, None, None, 'o')
        qdd.addTransition(qee, None, None, 'a')
        qee.addTransition(qff, None, None, 'n')
        qff.addTransition(qgg, None, None, 'e')
        qgg.addTransition(q2, None, None, 's')
        
        # U -> λ
        q2.addTransition(q2, None, 'U', None)
        
        q2.addTransition(q2, 's', 's', None)
        q2.addTransition(q2, 'e', 'e', None)
        q2.addTransition(q2, 'n', 'n', None)
        q2.addTransition(q2, 'a', 'a', None)
        q2.addTransition(q2, 'o', 'o', None)
        q2.addTransition(q2, '(', '(', None)
        q2.addTransition(q2, ')', ')', None)
        q2.addTransition(q2, '{', '{', None)
        q2.addTransition(q2, '}', '}', None)
        
        q2.addTransition(qf, None, '$', None)
        
        pda = PDA(q0)
        
        elapsed = time()
        
        Utils.checkout(pda.run(w),w)
        
        elapsed = time() - elapsed
        
        print(f'Tempo gasto: {elapsed:.3f}s')
            
    @staticmethod
    def calc(w: str):
        #  E -> T+E
        #  E -> T
        #  T -> F*E
        #  T -> F
        #  F -> a
        #  F -> (E)
        
        q0 = State('q0')
        q1 = State('q1')
        q2 = State('q2')
        qf = State('qf')

        qa = State('qa')
        qb = State('qb')
        qi = State('qi')
        qj = State('qj')
        qm = State('qm')
        qn = State('qn')
        
        qf.setFinal()

        q0.addTransition(q1, None, None, '$')
        q1.addTransition(q2, None, None, 'E')
        
        # E -> T+E
        q2.addTransition(qa, None, 'E', 'E')
        qa.addTransition(qb, None, None, '+')
        qb.addTransition(q2, None, None, 'T')

        # E -> T
        q2.addTransition(q2, None, 'E', 'T')

        # T -> F*E
        q2.addTransition(qi, None, 'T', 'E')
        qi.addTransition(qj, None, None, '*')
        qj.addTransition(q2, None, None, 'F')

        # T -> F
        q2.addTransition(q2, None, 'T', 'F')

        # F -> a
        q2.addTransition(q2, None, 'F', 'a')

        # F -> (E)
        q2.addTransition(qm, None, 'F', ')')
        qm.addTransition(qn, None, None, 'E')
        qn.addTransition(q2, None, None, '(')

        q2.addTransition(q2, 'a', 'a', None)
        q2.addTransition(q2, '+', '+', None)
        q2.addTransition(q2, '*', '*', None)
        q2.addTransition(q2, '(', '(', None)
        q2.addTransition(q2, ')', ')', None)

        q2.addTransition(qf, None, '$', None)

        pda = PDA(q0)
        
        elapsed = time()
        
        Utils.checkout(pda.run(w),w)
        
        elapsed = time() - elapsed
        
        print(f'Tempo gasto: {elapsed:.3f}s')

    @staticmethod
    def teste_y_x(w): # L = { w in Σ^* | w é um número binario multiplo de 3}
        q0 = State('q0')
        q1 = State('q1')
        q2 = State('q2')
        q0.setFinal()

        q0.addTransition(q0, '0', None, None)
        q0.addTransition(q1, '1', None, None)
        q1.addTransition(q0, '1', None, None)
        q1.addTransition(q2, '0', None, None)
        q2.addTransition(q2, '1', None, None)
        q2.addTransition(q1, '0', None, None)

        pda = PDA(q0)
        b = pda.run(w)
        
        elapsed = time()
        
        Utils.checkout(b, w)

    @staticmethod
    def reverso(w): #L = { ww^R | w in Σ^*={0,1}}
        q1 = State('q1')
        q2 = State('q2')
        q3 = State('q3')
        q4 = State('q4')
        q4.setFinal()
        
        q1.addTransition(q2, None, None, '$')	
        q2.addTransition(q2, '0', None, '0')
        q2.addTransition(q2, '1', None, '1')
        q2.addTransition(q3, None, None, None)
        q3.addTransition(q3, '0', '0', None)
        q3.addTransition(q3, '1', '1', None)
        q3.addTransition(q4, None, '$', None)

        pda = PDA(q1)
        b = pda.run(w)
        
        elapsed = time()
        
        Utils.checkout(b,w)
        
        elapsed = time() - elapsed
        
        print(f'Tempo gasto: {elapsed:.3f}s')