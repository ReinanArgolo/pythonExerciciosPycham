n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('insira a segunda nota do aluno: 3'))
media = (n1+n2)/2
if media < 5:
    print('REPROVADO'
          f'\nA média deste aluno foi {media}')
elif media >= 5 and media < 6.9:
    print("RECUPERAÇÃO"
          f'\nA média deste aluno foi {media}')
elif media == 7 or media > 7:
    print('APROVADO'
        f'\nA média deste aluno foi {media}')
