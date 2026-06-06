def aumentar(n = 0, i = 0):
    res = n * (1 + i/100)
    return res


def diminuir(n = 0, i = 0):
    res = n * (1 - i/100)
    return res


def dobro(n = 0):
    res = n * 2
    return res


def metade(n = 0):
    res = n / 2
    return res
    
    
def lin():
    print('=-=' * 25)


def moeda(p = 0, cambio = '', res = False):
    if res == True and cambio == '':
        cambio = 'R$'
        
    if res == True:
        if cambio == 'R$': 
            return f'{cambio}{p:.2f}'.replace('.', ',')
        else:
            return f'{cambio}{p:.2f}'
    if res == False:
        return f'{p:.2f}'
        

def resumo(p, ia, id, cambio, res):
    lin()
    print('Resumo Dos Valores'.center(75))
    lin()
    print(f'Preço Analisado: {moeda(p, cambio, res)}')
    print(f'Dobro do Preço: {moeda(dobro(p), cambio, res)}')
    print(f'Metade do Preço: {moeda(metade(p), cambio, res)}')
    print(f'{ia:.1f}% de Aumento: {moeda(aumentar(p, ia), cambio, res)}')
    print(f'{id:.1f}% de Decréscimo: {moeda(diminuir(p, id), cambio, res)}')
