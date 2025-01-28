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

    # Instances.fromGrammar('grammars/g1.txt', '000111')
    # Instances.fromGrammar('grammars/g1.txt', '000110')
    
    # Instances.fromGrammar('grammars/g2.txt', '(a+a)*(a+a)+(a*a)')
    # Instances.fromGrammar('grammars/g2.txt', '(a+))*(a+a)+(a*a)')
    
    # Instances.fromGrammar('grammars/g3.txt', '(a+a)*(a+a)+(a*a)')
    # Instances.fromGrammar('grammars/g3.txt', '((a+))*(a+a)+(a*a))')