from datetime import datetime
print('='*8, 'CONFEDERAÇÃO NACIONAL DE NATAÇÃO', '='*8)
data = int(input('Digite sua data de nascimento: '))
dataHj = datetime.today().year
idade = dataHj - data
if idade < 10:
    print('O aleta se enquadra na categoria: MIRIM')
elif idade > 9 and idade < 15:
    print('O aleta se enquadra na categoria: INFANTIL')
elif idade > 15 and idade < 20:
    print('O aleta se enquadra na categoria: JUNIOR')
elif idade == 20:
    print('O aleta se enquadra na categoria: SÊNIOR')
elif idade > 20:
    print('O aleta se enquadra na categoria: MASTER')
