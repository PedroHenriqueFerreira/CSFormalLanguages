from instances import Instances

if __name__ == "__main__": 
    Instances.teste_y_x('00001111')
    Instances.teste_y_x('00000001')
    
    Instances.reverso('1001001001')
    Instances.reverso('1001001000')
    
    Instances.calc('a*a+(a+a)')
    Instances.calc('a*a+(a+a(')
    
    Instances.enquanto('eqt(a){eqt(a){}}')
    Instances.enquanto('eqt(a){eqt(a){}{')
    
    Instances.se('se(a){se(a){}}senaose(a){}senao{}')
    Instances.se('se(a){se(a){}}senaose(a){}senao{{')

    Instances.fromGrammar('grammars/g1.txt', '000111')
    Instances.fromGrammar('grammars/g1.txt', '000110')
    
    Instances.fromGrammar('grammars/g2.txt', '(a+a)*(a+a)+(a*a)')
    Instances.fromGrammar('grammars/g2.txt', '(a+))*(a+a)+(a*a)')
    
    Instances.fromGrammar('grammars/g3.txt', '(a+a)*(a+a)+(a*a)')
    Instances.fromGrammar('grammars/g3.txt', '((a+))*(a+a)+(a*a))')
    
    Instances.fromGrammar('grammars/g4.txt', 'eqt(a){eqt(a){}}eqt(a){}')
    Instances.fromGrammar('grammars/g4.txt', 'eqt(a){eqt(a){}{')
    
    Instances.fromGrammar('grammars/g5.txt', 'se(a){se(a){}}senaose(a){}senao{}')
    Instances.fromGrammar('grammars/g5.txt', 'se(a){se(a){}}senaose(a){}senao{{') 
    
    Instances.fromGrammar('grammars/g6.txt', 'func(a,func(a),a);func(a,a);')
    Instances.fromGrammar('grammars/g6.txt', 'func(func(a),func(a),)')
    
    Instances.fromGrammar('grammars/g7.txt', 'trabalho1="automato_com_pilha";lfa_e_legal=verdade;pi=3.14')
    Instances.fromGrammar('grammars/g7.txt', '1trabalho="automato_com_pilha";lfa_e_legal=verdade;pi=3.14')