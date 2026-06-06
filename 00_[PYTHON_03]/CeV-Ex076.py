c = 0

list = ('Lápis', 1.75, 
        'Borracha', 2, 
        'Caderno', 15.90, 
        'Estojo', 25, 
        'Transferidor', 4.20, 
        'Compasso', 9.99, 
        'Mochila', 120.32, 
        'Caneta', 22.30, 
        'Livro', 34.90)
    
print('=-='*15)
print(f'{"Listagem de Preços":^45}')
print('=-='*15)

while c < len(list) : 
    
    if c % 2 == 0 : 
        print(f'{list[c]:.<30}', end = '')
    if c % 2 == 1 : 
        print(f'R${list[c]:>8.2f}')
    c += 1
    
print('=-='*15)