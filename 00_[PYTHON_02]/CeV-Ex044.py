
print('=========== Loja Giaretta ===========')

valor = float(input('Preço das Compras : '))

print('Formas de Pagamento : ')
print('[1] : À Vista Dinheiro/PIX')
print('[2] : À Vista no Cartão')
print('[3] : 2x no Cartão')
print('[4] : 3x ou mais no Cartão')
opcao = int(input('Qual Forma de Pagamento Deseja Escolher : '))

if opcao == 1 : 
    print('Voce Escolheu a Forma de Pagamento á Vista Dinheiro/PIX')
    print('Portanto Voce Receberá um Desconto de 10%')
    print(f'Sua Compra de R${valor:.2f} Saira Por R${valor*0.9:.2f}')
    
elif opcao == 2 : 
    print('Voce Escolheu a Forma de Pagamento á Vista Cartão')
    print('Portanto Voce Receberá um Desconto de 5%')
    print(f'Sua Compra de R${valor:.2f} Saira Por R${valor*0.95:.2f}')

elif opcao == 3 : 
    print('Voce Escolheu a Forma de Pagamento Em Até 2x no Cartão')
    print(f'Sua Compra de R${valor:.2f} Será Feita em 2 Parcelas de R${valor/2:.2f}')

elif opcao == 4 :
    parcelas = int(input('Em Quantas Vezes Deseja Parcelar a Compra : ')) 
    print(f'Sua Compra Será Parcelada em {parcelas}x de R${valor/parcelas:.2f} Com Juros')
    print(f'Sua Compra de R${valor:.2f} Saira Por R${valor*1.2:.2f} Ao Final')

else :
    print('Opção Invalida, Tente Novamente')






