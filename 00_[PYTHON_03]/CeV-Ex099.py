from time import sleep
def lin():
    print('=-='*15)
def maior(*num): 
    cont = maior = 0
    print('Analisando os Valores Passados...')
    for v in num:
        if v > maior:
            maior = v
    while cont < len(num):
        print(f'{num[cont]}', end = ' ')
        sleep(0.5)
        cont +=1
    print(f'Foram Informados {len(num)} Valores ao Todo.')
    print(f'O Maior Valor Informado Foi {maior}')
    lin()
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()