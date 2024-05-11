# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#- Para salários superiores a R$1250,00 calcule um aumento de 10%
#- Para os inferiores ou iguais o aumento é de 15%.
sal = float(input("Digite o salário deste funcionário: "))
if sal >= 1250.0:
    print(f'O aumento deste funcionário será de 10%, seu salario será de: {(sal*(10/100))+sal}')
else:
    print(f'O aumento do salário deste funcionário será de 15%, seu salário atual será de {(sal*(15/100))+sal}')