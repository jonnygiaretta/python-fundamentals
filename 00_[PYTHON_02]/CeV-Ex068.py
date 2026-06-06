
from random import randint

n = c = 0

print('=-='*10)
print('Vamos Jogar Par ou Impar')
print('=-='*10)


while True : 

    nc = randint(0, 10)
    n = int(input('Digite um Valor: '))
    pi = str(input('Par ou Impar [P/I]: ')).strip().upper()[0]

    if (n + nc) % 2 == 0 and pi in 'P' : 

        print('-'*30)
        print(f'Voce Jogou {n} e o Computador {nc}. Total deu Par.')
        print('-'*30)
        print('Voce Venceu')
        print('Vamos Jogar Novamente...')
        print('-'*30)
        c += 1 

    if (n + nc) % 2 == 1 and pi in 'I' : 

        print('-'*30)
        print(f'Voce Jogou {n} e o Computador {nc}. Total deu Impar.')
        print('-'*30)
        print('Voce Venceu')
        print('Vamos Jogar Novamente...')
        print('-'*30)
        c += 1 

    if (n + nc) % 2 == 0 and pi in 'I' : 

        print('-'*30)
        print(f'Voce Jogou {n} e o Computador {nc}. Total deu Impar.')
        print('-'*30)
        break

    if (n + nc) % 2 == 1 and pi in 'P' : 

        print('-'*30)
        print(f'Voce Jogou {n} e o Computador {nc}. Total deu Par.')
        print('-'*30)
        break

print('Voce Perdeu!')
print('=-='*10)
print(f'Game Over! Voce Venceu {c} Vezes.')
print('=-='*10)




