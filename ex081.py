numeros = []
numerosRevertidos = []

while True:
    numero = int(input('digite um Valor: '))
    numeros.append(numero)
    cond = input('Deseja continuar? [S/N]')

    if cond in 'Nn':
        break

quantidadeDigitada = len(numeros)
posCinco = numeros.index(5)
numeros.sort()
numeros.reverse()

print(f'Foram digitados {quantidadeDigitada} elementos')
print(f'Os valores em ordem decrescente são: ', numeros)
if 5 in numeros:
    print('O número cinco foi digitado e está na posição: ', posCinco)
else:
    print('O número cinco não foi difigtado, portanto, não está na lista')