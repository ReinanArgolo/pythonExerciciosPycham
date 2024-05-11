# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem de  zero até vinte.
# Seu programa deverá ler um número pelo teclado entre (0 e 20) e mostrá-lo por extenso.

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
escolha = int(input('Digite um número entre 0 e 20: '))
while escolha > 20:
    escolha = int(input('O número que você digitou é invalido, digite um numero entre 0 e 20: '))
print(f'Você digitou o número {numeros[escolha]}')