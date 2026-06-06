def lin():
    print('=-='*20)

def fatorial(n):
    s = 1
    print(f'Fatorial do Numero {n} Da-se da Seguinte Forma : ')
    for c in range(n, 0, -1):
        if n > 1 : 
            print(f'{n} x', end = ' ')
            s *= n 
        else : 
            print('1 = ', end = '')
        n -= 1
    return(s)
lin()
n = int(input('Deseja Saber o Fatorial de Qual Numero : '))
lin()
print(f'{fatorial(n)}')
lin()