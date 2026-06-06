
print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)

an = int(input('Quantos Termos Deseja Mostrar : '))

c = 1
a1 = 0
a2 = 1
s = 0



while c <= an : 

    print(f'{a1} -> ', end = '')

    s = a1 + a2 
    a1 = a2 
    a2 = s
    c += 1
    



print(end = '' 'Fim', )
print('-'*30)
