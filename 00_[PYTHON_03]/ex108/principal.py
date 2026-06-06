from funcoes import aumentar, diminuir, dobro, metade, lin, moeda

lin()
cambio = str(input('Deseja Fazer o Cambio em Qual Moeda[U.M//Padrão = R$]: '))
p = float(input('Digite o Valor do Produto: '))
id = float(input('Deseja Que o Desconto Seja de Quanto[%]: '))
ia = float(input('Deseja Que o Aumento Seja de Quantos[%]: '))
a = aumentar(p, ia)
d = diminuir(p, id)
aa = dobro(p)
dd = metade(p)

lin()

print(f'O Dobro de {moeda(p, cambio)} é {moeda(aa, cambio)}')
print(f'A Metade de {moeda(p, cambio)} é {moeda(dd, cambio)}')
print(f'Aumentando o Valor de {moeda(p, cambio)} em {ia}%, Temos o Valor: {moeda(a, cambio)} ')
print(f'Diminuindo o Valor de {moeda(p, cambio)} em {id}%, Temos o Valor: {moeda(d, cambio)} ')

lin()