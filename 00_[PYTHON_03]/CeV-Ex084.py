info = list()
group = list()
heavy = light = 0

print('=-='*10)

while True : 
    
    info.append(str(input('Nome [1ªN] : ')))
    info.append(float(input('Peso [Kg] : ')))
    
    if len(group) == 0 : 
        heavy = light = info[1]
    else : 
    
        if info[1] > heavy : 
            heavy = info[1]
        
        if info[1] < light :
            light = info[1]
            
    group.append(info[:])    
    info.clear()
        
    re = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    print('=-='*10)
    if 'N' in re : 
        break
    
print(f'Ao Todo Foram Cadastrados {len(group)} Pessoas')
print(f'O Maior Peso Cadastrado Foi {heavy}. Peso de : ')
for p in group : 
    if p[1]  == heavy : 
        print(f'[{p[0]}]', end = '; ')
print()
print(f'O Menor Peso Cadastrado Foi de {light}. Peso de : ')
for p in group : 
    if p[1]  == light : 
        print(f'[{p[0]}]', end = '; ')
print()
print('=-='*20)