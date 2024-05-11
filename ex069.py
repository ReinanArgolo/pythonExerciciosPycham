# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar, no final, mostre:
# a) quantas pessoas tem mais de 18 anos
# b) Quantos homens foram cadastrados.
# c) quantas mulheres tem menos de 20 anos.

maior = homens = mulheres = 0
while True:
    print('_'*30)
    print('     CADASTRE UMA PESSOA')
    print('_'*30)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F] ').upper().strip())
    while not sexo in 'MF':
        sexo = str(input('Sexo [M/F] ').upper().strip())
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulheres += 1

    print('_'*30)
    cond = input('Quer continuar? [S/N] ').upper().strip()
    while not cond in 'SN':
        cond = input('Quer continuar? [S/N] ').upper().strip()
    if cond == 'N':
        break

print('====== FIM DO PROGRAMA ======')
print(f'''Total de pessoas com mais de 18 anos: {maior};
Ao todo temos {homens} homens cadastrados;
E temos {mulheres} mulheres com menos de 20 anos.''')