from random import randint
drawn = list()
print('=-='*10)
print(f'{"Jogo da Mega-Sena":^30}')
print('=-='*10)
n = int(input('Quantos Jogos Você Deseja Que eu Sorteie ? '))
print(f'{" Sorteando " + str(n) + " Jogos ":=^30}')
for i in range(1, n+1) : 
    c = 0
    while True : 
        num = randint(1,60)
        if num not in drawn : 
            drawn.append(num)
            c += 1  
        if c >= 6 : 
            break
    drawn.sort()
    print(f'Jogo {i} : {drawn}')
    drawn.clear()
print(f'{" <//> Boa Sorte <\\> ":=^30}')