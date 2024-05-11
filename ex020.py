import random
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')
list = [a1, a2, a3, a4]
esco = random.sample(list, 4)
print(f'A ordem de apresentação será {esco}')
