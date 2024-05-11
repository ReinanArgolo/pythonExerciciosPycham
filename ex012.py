print('{:=^5} CALCULADORA DE PREÇOS (5%) {:=^5}'.format('',''))
vi = float(input('Qual o valor do produto? R$'))
por = 5/100
vpr = vi*por
vf = vi-vpr
print('Com o desconto de 5%, o produto passou a custar R${:.2f}\n'
      'Valor descontado = R${:.2f}'.format(vf, vpr))