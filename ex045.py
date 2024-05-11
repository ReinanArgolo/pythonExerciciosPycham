import random
itens = ('Pedra', 'Papel', 'Tesoura')
print('='*8, 'JOKENPÔ', '='*8)
p1 = random.randint(0,2)
p2 = int(input("0 - Pedra"
               "\n1 - Papel"
               "\n2 - Tesoura"
               "\nDIGITE SUA ESCOLHA: "))
if (p1 == 0 and p2 == 0) or (p1 == 1 and p2 == 1) or (p1 == 2 and p2 == 2):
    print("EMPATE")
elif (p1 == 0 and p2 == 2) or (p1 == 1 and p2 == 0) or (p1 == 2 and p2 == 0) or (p1 == 2 and p2 == 1):
    print('Você perdeu! :(')
elif (p1 == 2 and p2 == 0) or (p1 == 0 and p2 == 1) or (p1 == 0 and p2 == 2) or (p1 == 1 and p2 == 2):
    print('Você ganhou! :)')
else:
    print('Opção invalida, tente novamente!')

print(f'PC: {itens[p1]}'
      f'\nVOCÊ: {itens[p2]}')