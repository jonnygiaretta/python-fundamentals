def lin():
    print('=-='*15)
def ficha(nome = '<desconhecido>', gols = 0):
    lin()
    print(f'O Jogador {nome} Fez {gols} Gol(s) no Campeonato')
    lin()
lin()
nome = str(input('-> Nome do Jogador: '))
gols = str(input('-> Numero de Gol(s): '))
if gols.isnumeric():
    gols = int(gols)
else : 
    gols = 0
if nome.strip() == '':
    nome = '<desconhecido>'
ficha(nome, gols)