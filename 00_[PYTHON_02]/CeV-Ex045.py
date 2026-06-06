import time
import random

print('Suas Opções : ')
print('[0] Pedra')
print('[1] Papel')
print('[2] Tesoura')

opj = int(input('Qual a Sua Jogada : '))
oppc = random.randint(0, 2)

time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)

# Possibilidades Jogador Vence

if opj == 0 and oppc == 2:
    print('-=-'*5)
    print('Computador Jogou Tesoura')
    print('Jogador Jogou Pedra')
    print('Jogador Venceu')
    print('-=-'*5)

elif opj == 1 and oppc == 0:
    print('-=-'*5)
    print('Computador Jogou Pedra')
    print('Jogador Jogou Papel')
    print('Jogador Venceu')
    print('-=-'*5)

elif opj == 2 and oppc == 1:
    print('-=-'*5)
    print('Computador Jogou Papel')
    print('Jogador Jogou Tesoura')
    print('Jogador Venceu')
    print('-=-'*5)

# Possibilidades Computador Vence

if opj == 2 and oppc == 0:
    print('-=-'*5)
    print('Computador Jogou Pedra')
    print('Jogador Jogou Tesoura')
    print('Computador Venceu')
    print('-=-'*5)

elif opj == 0 and oppc == 1:
    print('-=-'*5)
    print('Computador Jogou Papel')
    print('Jogador Jogou Pedra')
    print('Computador Venceu')
    print('-=-'*5)

elif opj == 1 and oppc == 2:
    print('-=-'*5)
    print('Computador Jogou Tesoura')
    print('Jogador Jogou Papel')
    print('Computador Venceu')
    print('-=-'*5)

# Empate Entre Jogador e Maquina

elif opj == 0 and oppc == 0:
    print('-=-'*5)
    print('Computador Jogou Pedra')
    print('Jogador Jogou Pedra')
    print('Empate Entre Jogador e Computador')
    print('-=-'*5)

elif opj == 1 and oppc == 1:
    print('-=-'*5)
    print('Computador Jogou Papel')
    print('Jogador Jogou Papel')
    print('Empate Entre Jogador e Computador')
    print('-=-'*5)

elif opj == 2 and oppc == 2:
    print('-=-'*5)
    print('Computador Jogou Tesoura')
    print('Jogador Jogou Tesoura')
    print('Empate Entre Jogador e Computador')
    print('-=-'*5)

#Vazão a Possiveis Caso Bug

else:
    print('Algo Deu Errado, Tente Novamente')
