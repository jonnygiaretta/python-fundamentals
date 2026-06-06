vel = int(input('A Quantos Km/h Você Estava ? '))
dvel = (vel - 80)
valmul = dvel*7
print('-=-'*30)
if vel>80:
    print(f'Voce Será Multado por Estar a {vel} Km/h, {dvel} Km/h Acima do Limite Permitido de 80 Km/h\no Valor da Multa Será de R${valmul}')
else:
    print('Certo, Pode Seguir & Boa Viagem!')
print('-=-'*30)


