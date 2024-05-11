num = int(input('Insira o número a ser criptografado: '))
crpt = int(input('Selecione qual o método de crpitografia a ser utilizado: \n'
      '1 - binário\n'
      '2 - octal\n'
      '3 - hexadecimal\n'
                 'digite: '))
if crpt == 1:
    print(bin(num))
elif crpt == 2:
    print(oct(num))
elif crpt == 3:
    print(hex(num))