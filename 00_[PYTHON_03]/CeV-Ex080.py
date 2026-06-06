num = []
print('=-='*10)
for c in range (0,5): 
    n = int(input('Digite um Valor : '))
    if c == 0 or n > num[-1] : 
        num.append(n)
        print('Valor Adicionador ao Final da Lista.')
    else : 
        i = 0 
        while i < len(num) : 
            if n <= num[i] : 
                num.insert(i,n)
                print(f'Valor Adicionado na [{i+1}ª da Lista.]')
                break
            i += 1
    print('=-='*10)

print('=-='*10)
print(f'Os Valores Digitados em Ordem Foram : ')
print('=-='*10)
for a, b in enumerate(num): 
    print(f'O Valor [{b}] na [{a}]ª Posição')
print('=-='*10)