print('{:=^5} CONVERSOR DE MEDIDAS {:=^5}'.format('',''))
M = int(input('insira o valor em Metros a ser convertido: '))
Km = M/1000
hm = M/100
dam = M/10
dm = M*10
Cm = M*100
mm = M*1000
print(f'{M}m convertido nas seguintes unidades equivale a:\n'
      f'Km = {Km}\n'
      f'Hm = {hm}\n'
      f'Dam = {dam}\n'
      f'Dm = {dm}\n'
      f'CM = {Cm}\n'
      f'MM = {mm}')