runs = list()
info = dict()
print('=-='*15)
info['Nome'] = str(input('-> Nome do Jogador :  '))
n = int(input(f'-> Quantas Partidas {info['Nome']} Jogou ? '))
print('=-='*15)
for c in range(1, n+1):
    runs.append(int(input(f'-> Quantos Gols Fez na {c}ª Partida ? ')))
info['Gols'] = runs[:]
info['Total'] = sum(runs)
print('=-='*15)
print(f'O Jogador {info["Nome"]} Jogou {n} Partidas : ')
print('=-='*15)
for a, b in enumerate(info["Gols"]):
    print(f'=> Na {a+1}ª Foram Feitos {b} Gols')
print(f'Foram Feitos Um Total de {info["Total"]} Gols em {n} Partidas')
print('=-='*15)    