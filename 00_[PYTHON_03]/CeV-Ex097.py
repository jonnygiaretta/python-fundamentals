def escreva(msg) : 
    tam = len(msg) + 4
    print('=-=' * ((tam // 3)+1))
    print(f'   {msg:^{((tam // 3)+1)}}')
    print('=-=' * ((tam // 3)+1))

escreva('Gustavo Guanabara ')
escreva('Curso em Video de Python')
escreva('C&V')
