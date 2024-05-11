sexo = str(input('Digite o Sexo [M/F]: ')).strip().upper()
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido, digite um sexo válido!: '))
print("Fim")
