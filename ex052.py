num = int(input("Digite um número: "))
tot = 0
for i in range(1, num+1):
    if (num % i) == 0:
        print('\033[34m')
        tot += 1
    else:
        print('\033[m')
    print(f'{i}', end='')
if tot == 2:
    print(f'{num} um número primo!')
else:
    print('Este número não é primo!')