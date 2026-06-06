from random import randint
from time import sleep
nc = randint(0,5)

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('Vou Pensar Num Numero Entre 0 & 5. Tente Adivinhar')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
nu = int(input('Em Que Numero eu Pensei ? '))

print('Processando...')
sleep(2)

if (nu == nc):
    print('Parabens, Você Ganhou & Acertou')
else:
    print('Eu Ganhei, Você Perdeu & Errou')