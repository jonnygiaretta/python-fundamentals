from random import randint
from time import sleep
def lin():
    print('=-='*20)
def sorteia(num):
    lin()
    print('Os Valores Sorteados Foram :', end = ' ')
    for c in range(0, 5):
        n = randint(1,10)
        print(f'{n}', end = ' ')
        num.append(n)
        c += 1
    print('Finalizado!')
    lin()
def somapar(num):
    lin()
    s = 0
    for n in num:
        if n % 2 == 0 : 
            s += n
    print(f'A Soma Dos Valores Pares da Lista : {num}. Foi de {s}')
    lin()
num = list()
sorteia(num)
somapar(num)