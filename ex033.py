n1 = int(input('digite um número: '))
n2 = int(input('digite um número: '))
n3 = int(input('digite um número: '))
if n1 > n2 > n3:
    print(f'{n1} é o maior número!')
if n1 < n2 > n3:
    print(f'{n2} é o maior número')
if n1 < n2 < n3:
    print(f'{n3} é o maior número')