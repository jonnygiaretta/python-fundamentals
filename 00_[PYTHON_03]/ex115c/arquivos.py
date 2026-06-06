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
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<35}{dado[1]:>3} anos')
        a.close()

def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um Erro Na Abertura do Arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um Erro na Escrita do Arquivo.')
        else:
           print(f'Novo Registro de : {nome} Com {idade} Anos.') 
        finally:
           a.close()