import random

num = random.randint(1,5)
esc = int(input("Escolha um número entre 1 e 5: "))
if num == esc:
    print(f"Parabéns você acertou! O número era {esc}")
else:
    print("Você errou! :(")