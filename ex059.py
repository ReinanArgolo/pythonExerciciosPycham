from time import sleep
ch = 0
while ch != 5:
    v1 = int(input('Digite um valor: '))
    v2 = int(input('Digite outro valor: '))
    while ch != 5:
        print('''Escolha uma opção
        [1] SOMAR
        [2] MULTIPLICAR 
        [3] MAIOR
        [4] NOVOS NÚMEROS
        [5] SAIR DO PROGRAMA''')
        print('-'*50)

        esc = int(input('Digite sua escolha: '))
        print('-' * 50)
        if esc == 1:
            print(f'A soma entre {v1} e {v2} é igual a {v1+v2}')
        elif esc == 2:
            print(f'A multiplicação entre {v1} e {v2} é igual a {v1*v2}')
        elif esc == 3:
            if v1 > v2:
                print(f'{v1} é o maior valor')
            else:
                print(f'{v2} é o maior valor')
        elif esc == 4:
            print('Reiniciando programa...')
            sleep(1)
            v1 = int(input('Digite um valor: '))
            v2 = int(input('Digite outro valor: '))
        elif esc == 5:
            ch = 5
        elif esc > 5:
            print('Opção invalida, tente novamente!')
        print('-'*50)
        sleep(2)
print('Programa encerrado!')