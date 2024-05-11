# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (Numero inteiro)
# programa vai informar quantas cédulas de cada valor serão entregues.
# OBS. Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1

cin = vin = dez = um = falta = 0
print('='*30)
print('BANCO CEV'.center(30))
print('='*30)

while True:
    valor = int(input('Qual o valor deseja sacar? R$'))
    cin = valor // 50
    if (cin*50) < valor:
        falta = valor - (cin*50)
        vin = falta // 20
    if (vin*20 + cin*50) == valor:
            vin = vin
    if (vin*20 + cin*50) < valor:
            falta = falta - (vin*20)
            dez = falta // 10
    if (dez*10 + vin*20 + cin*50) == valor:
                dez = dez
    if (dez*10 + vin*20 + cin*50) < valor:
                falta = falta - (dez * 10)
                um = falta // 1

    if cin != 0:
        print(f'Total de {cin} cédulas de R$50,00')
    if vin != 0:
        print(f'Total de {vin} cédulas de R$20,00')
    if dez != 0:
        print(f'Total de {dez} cédulas de R$10,00')
    if um != 0:
        print(f'Total de {um} modedas de R$1,00''')

    break
print('='*30)
print('Volte sempre ao BANCO CEV! Volte Sempre!')
