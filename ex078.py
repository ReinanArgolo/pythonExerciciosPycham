numeros = list()
maior = 0
menor = 0

for cont in range(0,5):
    numeros.append(int(input(f'Digite um valor para a posição {cont}: ')))

for c, v in enumerate(numeros):
    if c == 0:
        maior = v
        menor = v
    else:
        if v >= maior:
            maior = v

        if v <= menor:
            menor = v

print('-=-'*20)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} e está nas posiçães', end = ' ')
for i, v in enumerate(numeros):
    if v == maior:
        print(i, end = '... ')
print(' ')
print(f'O menor valor digitado foi {menor} e está nas posições', end = ' ')
for i, v in enumerate(numeros):
    if v == menor:
        print(i, end = '... ')