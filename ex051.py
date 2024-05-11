a1 = int(input("Digite o primeiro termo desta PA: "))
r = int(input("Digite a Razão desta PA: "))
for i in range(0, 11):
    an = a1 + (i-1)*r
    print(f'a{i} = {an}')