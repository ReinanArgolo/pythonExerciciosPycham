s = 0
c = 0
for i in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
        c += 1
print(f'A soma dos {c} números é {s}!')