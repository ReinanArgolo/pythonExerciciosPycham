num = int(input('Escolha um número para encontrar seu fatorial: '))
c = num
f = 1
print(f'{num}! =', end=' ')
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -=1
print(f)