print('{:=^5} CALCULADORA DE REAJUSTE SALARIAL {:=^5}'.format('',''))
N = input('Nome do funcionário: ')
si = float(input('Digite o salário inicial de {}: R$'.format(N)))
acr = 15/100
soma = (si*acr)+si
print('O salário de {} após o reajuste será de R${:.2f}\n'
      'O acréscimo no salário foi de um valor real equivaleneta a R${:.2f}'.format(N, soma,soma-si))
