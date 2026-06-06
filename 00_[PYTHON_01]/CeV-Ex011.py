a = float(input('Qual a Altura(m) da Parede que Deseja Pintar : '))
l = float(input('Qual a Largura(m) da Parede que Deseja Pintar : '))

area = a * l 
ltinta = area/2

print('A Sua Parede Tem {} (m^2) & Você Precisara de {} (L) de Tinta Para Pinta-la'.format(area, ltinta))