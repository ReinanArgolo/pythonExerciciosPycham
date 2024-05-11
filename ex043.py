print('='*8, 'CALCULADORA DE IMC', '='*8)
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso/(altura**2)
print(f'Seu IMC (índice de massa corporal é de: {imc:.1f}')
if imc < 18.5:
    print('Atenção você está ABAIXO do peso!')
elif imc > 18.5 and imc < 25:
    print('Você está com o peso ideal')
elif imc > 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc > 30 and imc < 40:
    print('ATENÇÃO! Você está OBESO, Procure ajuda!')
elif imc > 40:
    print('Você possui OBESIDADE MORBIDA! procure ajuda especizalizada.')