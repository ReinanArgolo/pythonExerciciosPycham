dados = list()

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > dados[-1]:
        dados.append(n)
        print('Adiocionado ao final da lista')
    else:
        pos = 0
        while pos < len(dados):
            if n <= dados[pos]:
               dados.insert(pos, n)
               print(f'Adicionado na posição {pos}')
               break
            pos+=1

print('-='*30)
print(f'Os valores digitados em ordem foram: {dados}')