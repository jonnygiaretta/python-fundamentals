
n200 = n100 = n50 = n20 = n10 = n5 = 0
c100 = c50 = c25 = c10 = c5 = 0

print('='*30)
print('Banco JCG'.center(30))
print('='*30)

valor = int(input('Qual Valor Deseja Sacar : R$'))
t = len(str(valor))
c = (t - 1)

while c > 0:

    notas = 0
    notas = (valor // (10 ** c))
    nc = (notas * c)

    if c >= 3:
        n200 += nc / 200

    if c == 2:
        n200 += nc // 200
        n100 = (nc - (200 * n200)) // 100

    if c == 1:
        n50 = nc // 50
        n20 = (nc - (50 * n50))
        n10 = (nc - ((50 * n50) + (20 * n20)))
        n5 = (nc - ((50 * n50) + (20 * n20) + (10 + n10)))

    c += -1

print(f'{n200} {n100} {n50} {n20} {n10} {n5}')
