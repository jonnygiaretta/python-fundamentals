from math import sqrt

co = float(input('Qual o Comprimento do Cateto Oposto : '))
ca = float(input('Qual o Comprimento do Cateto Adjacente : '))
h = sqrt((ca**2)+(co**2))

print('O Triangulo Digitado Tem as Seguintes Medidas :')
print('Cateto Oposto : {}\nCateto Adjacente : {}\nPortanto Sua Hipotenusa Vale : {}'.format(co, ca, h))