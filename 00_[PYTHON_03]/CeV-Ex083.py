
print('=-='*10)
express = str(input('Digite a Expressão : '))

pyle = []

for symb in express : 
    if symb == '(' : 
        pyle.append('(')
    elif symb == ')' :  
        if len(pyle) > 0 : 
            pyle.pop()
        else : 
            pyle.append(')')
            break

print('=-='*10)        
if len(pyle) == 0 : 
    print('Sua Expressão Está Correta!')
else : 
    print('Sua Expressão Está Incorreta!')
print('=-='*10)
