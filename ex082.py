numeros = []
pares = []
impares = []


while True:
    usuario = int(input('Digite um número: '))
    numeros.append(usuario)

    condicao = input('Deseja continuar? [S/N]')
    if condicao in 'Nn':
        break

for c, v in enumerate(numeros):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)

print('Você digitou os números: ', numeros)
print(f'Destes números apenas {pares} são números pares')
print(f'Já {impares} são números impares.')