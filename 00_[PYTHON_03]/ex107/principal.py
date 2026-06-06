from funcoes import lin, aumentar, diminuir, dobro, metade 

lin()

p = float(input('Digite o Valor do Produto: '))
id = float(input('Deseja Que o Desconto Seja de Quanto[%]: '))
ia = float(input('Deseja Que o Aumento Seja de Quantos[%]: '))
a = aumentar(p, ia)
d = diminuir(p, id)
aa = dobro(p)
dd = metade(p)

lin()

print(f'O Dobro de R${p:.2f} é R${aa:.2f}')
print(f'A Metade de R${p:.2f} é R${dd:.2f}')
print(f'Aumentando o Valor de R${p:.2f} em {ia}%, Temos o Valor: R${a:.2f} ')
print(f'Diminuindo o Valor de R${p:.2f} em {id}%, Temos o Valor: R${d:.2f} ')

lin()
