nome = str(input('Digite o Seu Nome Completo : ').strip().title())
nomesplit = nome.split()

print(f'Muito Prazer em Te Conhecer {nome}')
print(f'Seu Primeiro Nome é  : {nomesplit[0]}')
print(f'Seu Ultimo Nome é : {nomesplit[len(nomesplit)-1]}')