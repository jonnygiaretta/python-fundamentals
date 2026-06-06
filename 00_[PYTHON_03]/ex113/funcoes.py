def lin():
    print('=-='*10)
    
def leiaint(msg):
    while True: 
        try: 
            ni = int(input(msg))
        except (ValueError, TypeError): 
            print('ERRO: Por Favor Digite um Valor Inteiro Valido.')
            lin()
            continue
        except (KeyboardInterrupt):
            print('O Usuario Preferiu Nâo Digitar Este Numero')
            return 0 
        else: 
            return ni 
            
            
def leiare(msg):
    while True: 
        try: 
            nr = float(input(msg)).replace(',','.')
        except (ValueError, TypeError): 
            print('ERRO: Por Favor Digite um Valor Real Valido.')
            lin()
            continue
        except (KeyboardInterrupt):
            print('O Usuario Preferiu Nâo Digitar Este Numero')
            return 0 
        else: 
            return nr