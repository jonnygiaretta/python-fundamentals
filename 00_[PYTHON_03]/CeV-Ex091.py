from random import randint
from time import sleep
from operator import itemgetter
game = list()
jogador = dict()
print('=-='*15)
for c in range(0,4) :
    jogador['Nome'] = str(input(f'Nome do {c+1}º Jogador : '))
    jogador['Valor'] = randint(1, 10)
    game.append(jogador.copy())
print('=-='*15)
for jogador in game : 
    print(f'Jogador(a) {jogador["Nome"]} Retirou o Valor : {jogador["Valor"]} ')
    sleep(0.5)
print('=-='*15)
print('  == Ranking Dos Jogares ==  ')
ranking = sorted(game, key = itemgetter('Valor'), reverse = True)
for a, b in enumerate(ranking) : 
    print(f'{a+1}º Lugar : {b["Nome"]}  Valor Retirado : {b["Valor"]} ')
    sleep(0.5)
print('=-='*15)
    