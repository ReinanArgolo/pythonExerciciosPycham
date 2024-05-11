s = 0
c = 0
for i in range(1, 501, 2):
        if i % 3 == 0:
            s += i
            c += 1
print(f'A soma dos {c} números impares múltiplos de 3 entre 1 e 500 é: {s}')