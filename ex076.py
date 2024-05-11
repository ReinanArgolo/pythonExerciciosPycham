#  = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120, 'Canetas', 22.3, 'Livro', 34.9)
valores = ('Lápis', '1.75', 'Borracha', '2.00', 'Caderno', '15.90', 'Estojo', '25.00', 'Transferidor', '4.20', 'Compasso', '9.99', 'Mochila', '120.00', 'Canetas', '22.3', 'Livro', '34.9')
print('-'*40,'\n',
    'LISTAGEM DE PREÇOS'.center(40), '\n'+
    '-'*40)
for i in range(0, len(valores), 2):
    print(f'{valores[i]}'+'.'*(30-(len(valores[i])))+'R$' + ' '*(7-len(valores[i+1]))+f'{valores[i+1]}')
print('-'*40)