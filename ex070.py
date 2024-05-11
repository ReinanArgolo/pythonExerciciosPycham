# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar no final, mostre:
# a) Qual é o total gasto na compra.
# b) Quantos produtos custam mais de R$1000
# c) qual é o nome do produto mais barato.

print('-'*30)
print('SUPER BARATÃO'.center(30))
print('-'*30)
c = valorTotal = maisQueMil = preçoBarato = nomeMB = 0

while True:
    nomeProduto = input('Nome do Produto: ')
    preço = float(input('Preço: R$'))
    cond = input('Deseja continuar? [S/N] ').upper().strip()
    while not cond in 'SNsn':
        cond = input('Deseja continuar? [S/N] ').upper().strip()
    valorTotal += preço
    c += 1
    if preço >= 1000:
        maisQueMil += 1


    if c == 1:
        preçoBarato = preço
        nomeMB = nomeProduto

    elif preço < preçoBarato:
        nomeMB = nomeProduto
        preçoBarato = preço

    print(' ')

    if cond == 'N':
        break
print('-'*10, 'FIM DO PROGRAMA', '-'*10)
print(f'''O total da compra foi {valorTotal:.2f}
Temos {maisQueMil} produtos custando mais que R$1000.00
O produto mais barato foi {nomeMB} que custa {preçoBarato:.2f}''')