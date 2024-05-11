kms = float(input("Qual a distância da viagem deste passageiro: "))
if kms <= 200:
    print(f"A o passageiro percorreu menos de 200Km, sua passagem custará R${kms * 0.50}")
else:
    print(f"A o passageiro percorreu mais de 200Km, sua passagem custará R${kms * 0.45}")