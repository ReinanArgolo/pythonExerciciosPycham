nome = str(input("Digite seu nome completo: "))
nome2 = nome.strip().upper().split()
answ = 'SILVA' in nome2
print(f'Seu nome possui silva? {answ}')