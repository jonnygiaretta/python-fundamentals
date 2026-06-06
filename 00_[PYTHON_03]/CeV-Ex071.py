
n200 = n100 = n50 = n20 = n10 = n5 = n1 = 0
c50 = c25 = c10 = c5 = c1 =  0

print('='*30)
print('Banco JCG'.center(30))
print('='*30)

valor = float(input('Qual Valor Deseja Sacar: R$'))
montante = valor

while True : 
    
    if montante >= 200 : 
        montante -= 200
        n200 += 1
    elif montante >= 100 : 
        montante -= 100
        n100 += 1
    elif montante >= 50 : 
        montante -= 50
        n50 += 1
    elif montante >= 20 : 
        montante -= 20
        n20 += 1
    elif montante >= 10 :
        montante -= 10
        n10 += 1
    elif montante >= 5 : 
        montante -= 5
        n5 += 1
    elif montante >= 1 : 
        montante -= 1
        n1 += 1
    else : 
        break

montante = int(round(montante * 100))

while True :   

    if montante >= 50 : 
        montante -= 50
        c50 += 1
    elif montante >= 25 : 
        montante -= 25
        c25 += 1
    elif montante >= 10 :
        montante -= 10
        c10 += 1
    elif montante >= 5 : 
        montante -= 5
        c5 += 1
    elif montante >= 1 : 
        montante -= 1
        c1 += 1
    else : 
        break


print('='*30)
print('Cedulas Totais'.center(30))
print('='*30)
print(f'Total de {n200} Cedulas de R$200')
print(f'Total de {n100} Cedulas de R$100')
print(f'Total de {n50} Cedulas de R$50')
print(f'Total de {n20} Cedulas de R$20')
print(f'Total de {n10} Cedulas de R$10')
print(f'Total de {n5} Cedulas de R$5')


print('='*30)
print('Moedas Totais'.center(30))
print('='*30)
print(f'Total de {n1} Moedas de R$1.00')
print(f'Total de {c50} Moedas de R$0.50')
print(f'Total de {c25} Moedas de R$0.25')
print(f'Total de {c10} Moedas de R$0.10')
print(f'Total de {c5} Moedas de R$0.05')
print(f'Total de {c1} Moedas de R$0.01')
print('='*30)



    
