num1 = int(input('Digite um número qualuquer: '))
num2 = int(input('Digite outro número qualuquer: '))
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num1 < num2:
    print(f'{num1} é menor que {num2}')
elif num1 == num2:
    print('Não há número maior, os dois são iguais.')

