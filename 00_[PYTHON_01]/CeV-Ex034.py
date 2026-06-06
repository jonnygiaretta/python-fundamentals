salario = float(input(f'Digite o Valor de Seu Salario : R$ '))

salarioup = salario * 1.10 if salario > 1250 else salario * 1.15
diferenca = salarioup - salario

print('-=-'*30)
print(f'Parabens!, Você Recebeu um Aumento!\nSeu Salario Foi de R${salario:.2f} Para R${salarioup:.2f}, Totalizando um Aumento de R${diferenca:.2f}')
print('-=-'*30)