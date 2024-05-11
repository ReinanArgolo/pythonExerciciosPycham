dados = list()
numAnterior = 0
for cout in range(0, 5):
    num = int(input('Digite um número: '))
    if cout == 0:
        dados.append(num)
        numAnterior = num
    else:
        if num < numAnterior:
            id = dados.index(numAnterior)
            dados.insert(id, num)

print(dados)