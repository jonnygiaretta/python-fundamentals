d = int(input('Quantos Dias Você Ficou Com o Carro : '))
km = float(input('Quantos Km Você Rodou Com o Carro : '))

v = ((d*60) + (km*0.15))

print('O Valor a Ser Pago Por Ter Alugado o Carro {} Dias & Rodado {} Km Será de {}R$'.format(d, km, v))