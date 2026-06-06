def arquivoexiste(arq):
    try:
        a = open(arq, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
        
def criararquivo(arq):
    try:
        a = open(arq, 'wt+')
        a.close()
    except:
        print('Houve Um Erro Na Criação do Arquivo!')
    else:
        print(f'O Arquivo de Nome: {arq}, Foi Criado!')
        
def lerarquivo(arq):
    try:
        a = open(arq, 'rt')
    except:
        print('Erro Ao Ler o Arquivo!')
    else:
        print(a.read())
        a.close()
