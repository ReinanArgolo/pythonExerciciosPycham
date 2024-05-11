num1 = int(input('Digite um valor: '))
num2 = int(input('Digite um valor: '))
num3 = int(input('Digite um valor: '))
num4 = int(input('Digite um valor: '))
valor = (num1, num2, num3, num4)
pares = 0
print(f'O valor nove apareceu {valor.count(9)} vezes.')
if 3 in valor: print(f'O numero 3 aparece a primeira vez na {valor.index(3)+1} posição')
else: print('O numéro três não foi digitado!')
for i in valor:
    if i % 2 == 0:
        pares +=1
if pares > 0:
    print('Os valores pares digitados foram: ', end=' ')
    for i in valor:
        if i % 2 == 0:
            print(i, end=' ')
else:
    print('Não foram digitados valores pares')