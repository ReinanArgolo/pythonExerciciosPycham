from time import sleep
números = list()
while True:
    numDigi = int(input('Digite um número: '))
    if numDigi not in números:
        números.append(numDigi)
        print('Valor adicionado com sucesso!')
    else:
        print('Duplicado adicionado! Não vou adicionar.')
    condição = input('Deseja continuar? [S/N] ').upper().strip()
    if condição == 'N':
        break
    else:
        print('-'*25)

print('Você digitou os valores: ', sorted(números))