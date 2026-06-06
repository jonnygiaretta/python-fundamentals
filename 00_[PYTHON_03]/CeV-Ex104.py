def lin() : 
    print('=-='*15)

def leiaint():
    n = str(input('-> Digite um Numero: '))
    while True : 
        if n.isnumeric():
            n = int(n)
            return n
        else : 
            lin()
            print('Digitação Incorreta! Por Favor Digite um Numero Inteiro Valido')
            n = str(input('-> Digite um Numero: '))

lin()
n = leiaint()
lin()
print(f'-> Você Acabou de Digitar o Numero : {n}')
lin()