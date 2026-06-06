casa = float(input('Digite o Valor Da Casa que Deseja Comprar : '))
salario = float(input('Digite o Valor de Seu Salario : '))
tempo = float(input('Digite Em Quantos Anos Pretende Pagar a Casa : '))
parcela = ((casa/tempo)/12)

if (salario/12*tempo) >= (salario/3):
    print(f'Para Pagar a Casa no Valor de R$ {casa:.2f} em {tempo:.2f} Anos')
    print(f'Sua Parcela Será de R$ {parcela:.2f} e Portanto Seu Financiamento Será Aprovado')
    print('Por Favor Prossiga Para o Guichê')

else:
    print(f'Para Pagar a Casa no Valor de R$ {casa:.2f} em {tempo:.2f} Anos')
    print(f'Sua Parcela Será de R$ {parcela:.2f} e Portanto Seu Financiamento Será Aprovado')
    print('Por Favor, Tente Novamente ')