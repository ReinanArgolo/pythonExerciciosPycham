from random import randint
num = randint(0,10)
esc = (int(input('Tente acertar o número que o computador escolheu: ')))
t = 0
while num != esc:
    if esc > num:
        print('Menos...')
    elif esc < num: print('Mais...')
    esc = int(input('Tente novamente: '))
    t = t + 1
print(f'Parabéns você acertou! Você tentou {t} vezes!')