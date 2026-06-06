ano = int(input('Qual Ano Deseja Saber Se é Bissexto : '))

if (ano % 100==0):
    verificador = (ano % 400==0)
if (ano % 4 ==0):
    verificador = bool(True)
else:
    verificador = bool(False)

print('-=-'*20)
print(f'O Ano {ano} Que Você Digitou é Bissexto : {verificador}')
print('-=-'*20)