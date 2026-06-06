from time import sleep
def lin():
    print('=-='*15)
def cont(a, b, c) : 
    lin()
    print(f'Contagem de {a} até {b}, Passo de {c} em {c}')
    for n in range(a, b, c):
        print(n, end = ' ')
        sleep(0.5)
    print('Fim! ')
    lin()
        
cont(1, 10, 1)
cont(10, 0, -2)
print('Agora é Sua Vez de Personalizar a Contagem')
a = int(input('Inicio: '))
b = int(input('Final: '))
c = int(input('Passo: '))
if a > b : 
    cont(a, b, -c)
else : 
    cont(a, b, c)