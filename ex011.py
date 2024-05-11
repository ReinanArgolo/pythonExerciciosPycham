print('{:=^5} CALCULADORA DE TINTA {:=^5}'.format('',''))
alt = float(input('Qual a altura da parede? '))
lar = float(input('Qual a largura da parede? '))
area = alt*lar
print("A parede possui {}m²".format(area))
print('Sabendo que cada litro de tinta pinta 2m²,'
      'Desta forma chegamos a conclusão que serão necessários {:.2f} litros de tinta!'.format(area/2))