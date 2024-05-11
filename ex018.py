import math
ang = float(input('digite o ângulo do triângulo retângulo: '))
rad = math.radians(ang)
print(f'O triângulo {ang}º possui: \n'
      f'Senº = {math.sin(rad):.2f}\n'
      f'Cosº = {math.cos(rad):.2f}\n'
      f'Tanº = {math.tan(rad):.2f}')