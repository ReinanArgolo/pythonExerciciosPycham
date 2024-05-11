t1 = 0
t2 = 1
n = int(input('Digite a quantidade de termos a serem mostradas: '))
c = 1
while c <= n:
    t3 = t1 + t2
    print(f'{t3} - ', end = '')
    t1 = t2
    t2 = t3
    c+=1
print('FIM')