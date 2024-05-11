# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre:
# - a média de idade do grupo;
# - qual é o nome do homem mais velho;
# - quantas mulheres têm menos de 20 anos.


media = 0
idadeHV = 0
nomeHV = 0
mulheres_20_anos = 0

for i in range(1, 5):
    print('-'*5, f'{i}ª PESSOA', '-'*5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()

    media += idade

    if idade > idadeHV and sexo == 'M':
        nomeHV = nome
        idadeHV = idade

    if idade < 20 and sexo == 'F':
        mulheres_20_anos += 1
media = media/4
print(f'A média de idade do grupo informado é de {media};')
print(f'O homem mais velho do grupo é {nomeHV}, e ele tem {idade};')
print(f'Ao todo {mulheres_20_anos}, são menores de 20 anos!')