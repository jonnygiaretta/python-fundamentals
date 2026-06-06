matrix = [[], [], []]
p = t = s = 0
print('=-='*15)
for a in range (0,3) : 
    for b in range(0,3) : 
        n = int(input(f'Digite um Valor Para [{a}, {b}]: ' ))
        if n % 2 == 0 :
            p += n 
        if b == 2 : 
            t += n
        if a == 1 and n > s : 
            s = n
        matrix[a].append(n)
print('=-='*15)
for a in range (0,3) : 
    for b in range(0,3) : 
        print(f'[{matrix[a][b]:^5}]', end = ' ')
    print()
print('=-='*15)
print(f'A Soma Dos Valores Pares : {p}')
print(f'A Soma Dos Valores da Terceira Coluna : {t}')
print(f'O Maior Valor da Segunda Linha : {s}')
print('=-='*15)