a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a Razão desta PA: '))
n = 1
ad = 1
while n > 0:
    for i in range(1, 10+ad):
        an = a1 + (i - 1) * r
        print(f'a{i} = {an}')
    n = int(input('Quantos termos mais deseja msotrar: '))
    ad += n
print(f'Fim do programa! foram mostrados {ad+9} termos')