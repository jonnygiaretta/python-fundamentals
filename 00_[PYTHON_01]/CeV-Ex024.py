cidade = input('Qual o Nome de Sua Cidade : ').title()
catc = cidade.split()
verificador = 'Santo' in catc[0]

print(f'A Cidade Digitada {cidade}, Possui "Santo" em Seu Nome : {verificador}')