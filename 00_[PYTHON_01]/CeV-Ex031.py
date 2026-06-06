d = int(input('Para Saber o Valor de Sua Passagem, Digite o Total de Km que Deseja Viajar : '))

val = d * 0.5 if d<=200 else d * 0.45
print('-=-'*30)
print('Obrigado Por Escolher Viajar Conosco')
print(f'Você Deseja Viajar {d}(Km) & Sua Passagem Custará R${val:.2f}')
print('-=-'*30)
