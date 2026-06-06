matrix = [[], [], []]
print('=-='*10)
for a in range (0,3) : 
    for b in range(0,3) : 
        n = int(input(f'Digite um Valor Para [{a}, {b}]: ' ))
        matrix[a].append(n)
print('=-='*10)
for a in range (0,3) : 
    for b in range(0,3) : 
        print(f'[{matrix[a][b]}:^5]', end = ' ')
    print()
print('=-='*10)