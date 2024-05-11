from random import randint
print('=-'*15 )
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*15 )
vitoria = 0

while True:
    pc = randint(0,10)
    nplayer = int(input('Diga um valor: '))
    esc = str(input('Par Ou Ímpar? [P/I] ')).upper().strip()
    while not esc in 'PIip':
        esc = str(input('Par Ou Ímpar? [P/I] ')).upper().strip()
    print('-'*30)

    soma = pc + nplayer

    if (soma % 2) == 0:
        if esc == 'P':
            print(f'Você jogou {nplayer} e o computador {pc}. A soma foi igual a {soma} que é PAR')
            print('-' * 30)
            print('Você venceu, vamos jogar novamente!')
            vitoria +=1
        elif esc == 'I':
            print(f'Você jogou {nplayer} e o computador {pc}. A soma foi igual a {soma} que é PAR')
            print('-' * 30)
            print('Você perdeu!')
            break
    if (soma % 2) != 0:
        if esc == 'I':
            print(f'Você jogou {nplayer} e o computador {pc}. A soma foi igual a {soma} que é IMPAR')
            print('-' * 30)
            print('Você venceu, vamos jogar novamente!')
            vitoria += 1
        if esc == 'P':
            print(f'Você jogou {nplayer} e o computador {pc}. A soma foi igual a {soma} que é ÍMPAR')
            print('-' * 30)
            print('Você perdeu!')
            break
print(f'GAME OVER! Você venceu {vitoria} vezes.')