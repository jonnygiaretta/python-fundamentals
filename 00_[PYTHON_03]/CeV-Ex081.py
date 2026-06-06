num = []
print('=-='*20)
while True : 
    n = int(input('Digite um Valor : '))
    num.append(n)
    
    re = str(input('Deseja Continuar [S/N] : '))
    re = re.strip().upper()[0]
    
    if 'N' in re : 
        break
    else : 
        while True : 
            print('Comando de Continuidade Incorreto! Digite Novamente.')
            re = str(input('Deseja Continuar [S/N] : '))
            re = re.strip().upper()[0]
            if 'N' in re : 
                break
            
num = num.sort(reverse=True)
    
print('=-='*20)
print('Os Numeros Digitados em Ordem Decrescentes São :')
print('=-='*20)
for i, n in enumerate(num) : 
    print(f'Numero [{n}] // [{i+1}]ª Posição')
print('=-='*20)
print(f'Voce Digitou {i+1} Valores ao Total.')
if 5 in num :
    print('O Valor 5 Faz Parte da Sua Lista')
else : 
    print('O Valor 5 Não Faz Parte da Sua Lista')
print('=-='*20)