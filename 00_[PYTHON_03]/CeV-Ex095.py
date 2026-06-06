geral = list()
gols = list()
player = dict()
re = 'S'
print('=-='*15)
while True : 
    player.clear()
    gols.clear()
    player['Nome'] = str(input('-> Nome do Jogador :  '))
    n = int(input(f'-> Quantos Jogos o Jogador {player['Nome']} Jogou : '))
    print('=-='*15)
    for c in range(1, n+1):
        gols.append(int(input(f'-> Quantos Gols Fez na {c}ª Partida ? ')))
    print('=-='*15)
    player['Gols'] = gols[:]
    player['Total'] = sum(gols)
    geral.append(player.copy())
    re = str(input('-> Deseja Continuar [S/N] : ')).strip().upper()[0]
    print('=-='*15)
    while re not in 'SN' : 
        print('-> Comando de Continuidade Digitado Incorretamente')
        re = str(input('-> Deseja Continuar [S/N] : ')).strip().upper()[0]
        if re in 'SN' : 
            break
    if re == 'N':
        break
print(f'{"Cod":<4} {"Nome":<15} {"Gols":<15} {"Total":<5}')
print('=-='*15)
for a, b in enumerate(geral) : 
    print(f'{(a+1):<4} {b["Nome"]:<15} {str(b["Gols"]):<15} {b["Total"]:<5}')
print('=-='*15)
while True:
    num = int(input('-> Deseja Mostrar os Dados de Qual Jogador [999/Encerrar] : '))
    num -= 1
    if num == 998 : 
        break
    print('=-='*15)
    while num not in range(0, len(geral)):
        print('-> Comando de Selecionamento de Jogador Incorreto, Por Favor Digite Novamente')
        num = int(input('-> Deseja Motrar os Dados de Qual Jogador [999/Encerrar] : '))
        if num in range(0, len(geral)) : 
            break
    print(f'{geral[num]["Nome"]:<15} {str(geral[num]["Gols"]):<15} {geral[num]["Total"]:<5}')
    print('=-='*15)
print('=-='*15)
print(f'{"<< Encerrando Programa >> ":^45}')
print('=-='*15)
