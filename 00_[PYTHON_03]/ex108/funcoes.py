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
    print('=-='*20)


def moeda(p = 0, cambio = 'R$'):
    if cambio == '':
        cambio = 'R$'
    if cambio == 'R$': 
        return f'{cambio}{p:.2f}'.replace('.', ',')
    else:
        return f'{cambio}{p:.2f}'