a = float(input('Digite o Valor do Primeiro Segmento do Triangulo : '))
b = float(input('Digite o Valor do Segundo Segmento do Triangulo : '))
c = float(input('Digite o Valor do Terceiro Segmento do Triangulo : '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print('-=-'*25)
    print(
        f'os Segmentos de Reta : {a:.3f}, {b:.3f} e {c:.3f} Formam um Triangulo')
    print('-=-'*25)
else:
    print('-=-'*25)
    print(
        f'os Segmentos de Reta : {a:.3f}, {b:.3f} e {c:.3f} Não Formam Triangulo')
    print('-=-'*25)
