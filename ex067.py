while True:
    num = int(input('Digite o número que quer mostrar a tabuada: '))
    print('-'*45)
    if num < 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {i*num}')
    print('-'*45)
