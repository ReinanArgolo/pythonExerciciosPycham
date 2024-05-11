# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime
data = datetime.today().year
cntP = 0
menores = 0
maiores = 0
for p in range(0, 7):
    cntP = cntP + 1
    AnoP = int(input(f"Dogite o ano da {cntP}ª pessoa: "))
    idade = data - AnoP
    if idade < 21:
        menores = menores + 1
    else:
        maiores = maiores + 1
print(f'Ao todo tivemos {maiores} pessoas maiores de idade, e {menores} pessoaas menores de idade! ')
