a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a Razão desta PA: '))
n = 1
while n < 10:
    n += 1
    an = a1 + (n-1) * r
    print(f'{an}', end=' → ')
print('FIM')