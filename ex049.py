print('='*20, 'TABUADA', '='*20)
n = int(input("Digite  o número que você quer saber a tabuada: "))
for i in range(1, 11):
    print(f'{n} x {i} = {n*i}')