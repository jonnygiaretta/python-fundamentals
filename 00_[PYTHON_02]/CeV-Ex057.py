
sexo = str(input('Informe o Seu Sexo [M/F] : ')).upper().strip()[0]

while sexo not in 'MmFf' : 
    sexo = str(input('Dados Invalidos, Por Favor Informe o Seu Sexo Corretamente : ')).upper().strip()[0] 

print(f'Sexo {sexo} registrado com Sucesso')
