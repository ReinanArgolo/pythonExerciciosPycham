num = 0
cont = 0
soma = 0
num = int(input('Digite um número qualquer: '))
while num != 999:
    cont+=1
    soma += num
    num = int(input('Digite um número qualquer: '))
print(f'Foram digitados {cont} numeros, e a soma foi igual a: {soma}')