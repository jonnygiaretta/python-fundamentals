
c = 1
n = 0

while True : 
    n = int(input('Deseja Ver a Tabuada de Qual Valor : ')) 
    c = 1
    print('-'*20)
    if n < 0 : 
        break
    

    while c <= 10 : 
        print(f'{n} x {c} = {n*c}')
        c += 1
    print('-'*20)
        
    
print('Programa de Tabuada Encerrado, Por Favor Volte Sempre!')
