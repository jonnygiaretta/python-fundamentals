from random import randint
from time import sleep

def lin() :
    print('=-='*30)
    
def sorteia(num) :
    lin()
    r = int(input('Deseja Analisar Quantas Rodadas de Somas Pares Aleatorias : '))
    p = int(input('Deseja Que Sejam Sorteados Quantos Numeros Por Rodada ? '))
    i = int(input('Deseja Que o inicio Da Lista Se Dem em Qual Numero ? '))
    f = int(input('Deseja Que o Final da Lista Se Dem em Qual Numero ? '))
    for t in range (0, r) :
        lin()
        print(f'Sorteando {p} Valores Da Lista : ', end ='')
        row = list()
        for c in range (0,p): 
            n = randint(i,f)
            num.append(n)
            row.append(n)
        print(f'{row}', end = ' ')
        print('Finalizado.')
        lin()

def somapar(num, nump):
    s = 0
    for v in num : 
        if v % 2 == 0 :
            s += v
            nump.append(v)
    
    totalelementos = len(num)
    totalpares = len(nump)
    pctpares = (totalpares / totalelementos) * 100
    pctimpares = 100 - pctpares
            
    print(f'Somando os Valores Pares de Todas as Listas Temos a Lista Par: \n-> : {nump} .')
    print(f'-> Totalizando o Valor de [{s}] em Seu Somatorio.')
    print(f'-> Proporção: [{pctpares:.2f}%] de Pares & [{pctimpares:.2f}%] de Ímpares.')
    print(f'-> No Total de {totalelementos} Números de Espaço Amostral.') 
    lin()
num = list()
nump = list()
sorteia(num)
somapar(num, nump)