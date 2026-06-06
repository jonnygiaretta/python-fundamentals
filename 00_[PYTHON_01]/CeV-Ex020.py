from random import shuffle
n1 = str(input('Qual o Nome do Primeiro Aluno : '))
n2 = str(input('Qual o Nome do Segundo Aluno : '))
n3 = str(input('Qual o Nome do Terceiro Aluno : '))
n4 = str(input('Qual o Nome do Quarto Aluno : '))

lista = [n1, n2, n3, n4]
shuffle(lista)

print('A Ordem de Apresentação Será : ')
print(lista)