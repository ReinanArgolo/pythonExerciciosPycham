print('{:=^5} CARTEIRA DIGITAL {:=^5}'.format('',''))
V = float(input('Quantos reais você possui? '))
print('Seu saldo atual é de R${}\n'
      'Este valor equivale a ${:.2f} dólares'.format(V, V/3.27))
print('Este valor possui por base a cotação de 2017!')
