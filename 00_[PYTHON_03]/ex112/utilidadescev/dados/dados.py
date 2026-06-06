def leiadinheiro(p): 
    while True: 
        n = str(input(p)).strip().replace(',','.')
        if n.replace('.','').isnumeric() and n != '':
            return float(n)
        else:  
            print(f'Valor Digitado : "{n}" Invalido! Digite Novamente.')