# ler num
# mostrar média
# mostrar maior e menor valor

soma = 0
c = 0
num = 0
maior = 0
menor = 0
flag = ''
while not flag == 'N':
    num = int(input('digite um número: '))
    soma += num
    c += 1

    if c == 1:
        maior = num
        menor = num
    elif maior < num:
        maior = num
    elif menor > num:
        menor = num
    flag = str(input('DESEJA CONTINUAR [S/N]: ')).upper().strip()
media = soma/c
print(f'''A média dos números digitados foi: {media}!
O maior número digitado foi: {maior}
O menor número digitado foi {menor}''')