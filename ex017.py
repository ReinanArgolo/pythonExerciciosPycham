import math
print('='*5, 'CALCULADORA DA HIPPOTENUSA', '='*5)
cat1 = float(input('Digite o valor do cateto opsoto: '))
cat2 = float(input('Digite o valor do cateto adjascente: '))
qrhip = (cat1.__pow__(2)) + (cat2.__pow__(2))
sqrthip = math.sqrt(qrhip)
print(f'O valor da hipotenusa do triangulo que possui os valores respectivos de seus catetos {cat1} e {cat2} é igual a: {sqrthip}')