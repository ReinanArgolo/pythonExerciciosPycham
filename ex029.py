kms = int(input("Qual a velociade do carro em KMs/h: "))
if kms <=  80:
    print("O carro está dentro da velociade permitida!")
else:
    print(f'''O carro está acima da velociddade permitida
    O valor da multa será de R${(kms - 80)*7}''')