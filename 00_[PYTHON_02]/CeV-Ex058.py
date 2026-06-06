
from random import randint
from time import sleep

n = randint(1, 10)
tentativas = 1

print('Sou Seu Computador...')
sleep(1)
print('Acabei de Pensar em Um Numero Entre 0 a 10')
sleep(1)
print('Consegue Adivinhar Qual Numero Foi ?')

a = int(input('Qual é Seu Palpite  : '))

while a != n : 

    tentativas += 1
    if a < n : 
        print('Mais... Tente Mais uma Vez')
        a = int(input('Qual é Seu Palpite  : '))
    if a > n : 
        print('Menos... Tente Mais uma Vez')
        a = int(input('Qual é Seu Palpite  : '))

print(f'Acertou com {tentativas}. Parabéns!')