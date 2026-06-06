def lin():
    print('=-='*20)
    
def notas(*g, sit = False):
    g = list(g)
    n = dict()
    nome = str(input('-> Digite o Nome do Aluno: '))
    lin()
    n['nome'] = nome
    n['notas'] = g
    n['total'] = len(g)
    n['maior'] = max(g)
    n['menor'] = min(g)
    n['media'] = sum(g)/len(g)
    #Sistema de Notas Utilizado Internamente no ITA
    if sit == True : 
        if n['media'] > 9.5:
            n['situacao'] = 'Louvor'
        elif n['media'] > 8.5: 
            n['situacao'] = 'Muito Bom'
        elif n['media'] > 7.5:
            n['situacao'] =  'Bom'
        elif n['media'] > 6.5:
            n['situacao'] =  'Regular'
        elif n['media'] > 5:
            n['situacao'] =  'Insuficiente'
        else :
            n['situacao'] = 'Deficiente'
    else:
        n['situacao'] = 'Não informada'
        

    return n  
lin()
c = int(input('-> Deseja Fazer Upload de Quantas Notas: '))
lin()
num = list()
for i in range(0,c):
    nota = float(input(f'-> Digite a {i+1} Nota: '))
    num.append(nota)
lin()
n = notas(*num, sit = True)
print(f'< O Aluno {n["nome"]} No Total de {n["total"]} Periodos Letivos >')
lin()
print(f'-> Teve as Seguintes Notas: {n["notas"]}')
lin()
print(f'-> Media do Aluno {n["nome"]} nos {n["total"]} Periodos Letivos : {n["media"]:.1f}')
lin()
print(f'-> Maior & Menos Nota do Aluno {n["nome"]} Respectivamente : {n["maior"]} & {n["menor"]}')
lin()
print(f'-> Situação do Aluno {n["nome"]} : {n["situacao"]}')
lin()