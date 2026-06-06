a = float(input('Digite o Valor do Primeiro Segmento do Triangulo : '))
b = float(input('Digite o Valor do Segundo Segmento do Triangulo : '))
c = float(input('Digite o Valor do Terceiro Segmento do Triangulo : '))

if (a + b) > c and (a + c) > b and (b + c) > a:
    print(f'os Segmentos de Reta : {a:.2f}, {b:.2f} e {c:.2f} Formam um Triangulo')
    
    if a == b and b == c and a == c :
        print(f'os Segmentos do Triangulo : {a:.2f}, {b:.2f} e {c:.2f} : Formam um Triangulo Equilátero.')

    elif a != b and b != c and a != c :
        print(f'Os Segmentos do Triangulo : {a:.2f}, {b:.2f} e {c:.2f} : Formam um Triangulo Escaleno')

    elif a == b or a == c or a == c :
        print(f'Os Segmentos do Triangulo : {a:.2f}, {b:.2f} e {c:.2f} : Formam um Triangulo Isósceles')
    
else:
    print(f'os Segmentos de Reta : {a:.2f}, {b:.2f} e {c:.2f} Não Formam Triangulo')