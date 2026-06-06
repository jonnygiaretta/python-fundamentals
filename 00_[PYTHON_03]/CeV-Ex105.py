def notas(*g, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param g: Uma ou mais notas dos alunos (aceita quantas precisar).
    :param sit: (Opcional) Indica se deve ou não adicionar a situação.
    :return: Dicionário com o total de notas, maior, menor, média e situação.
    """
    n = dict()
    n['total'] = len(g)
    n['maior'] = max(g)
    n['menor'] = min(g)
    n['media'] = sum(g) / len(g)
    
    if sit == True:
        if n['media'] > 7:
            n['situacao'] = 'Aprovado'
        elif n['media'] >= 5:
            n['situacao'] = 'Razoavel'
        else:
            n['situacao'] = 'Reprovado'
            
    return n
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
# help(notas)