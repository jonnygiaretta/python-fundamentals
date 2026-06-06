
d = 0

n = int(input('Digite um Numero : '))

for c in range(1,n+1):
    if n % c == 0:
        print('\033[33m', end= ' ')
    else : 
        print('\033[31m', end= ' ')

    print(c, end=' ')

    if n % c == 0 :
        d = d + 1

print('\033[m', end= ' ')
print(f'\nO Numero {n} Foi Divisivel {d} Vezes')
if d == 2 : 
    print(f'E Por Isto {n} é um Numero Primo')
else:
    print(f'E Por Isto {n} Não é um Numero Primo')

