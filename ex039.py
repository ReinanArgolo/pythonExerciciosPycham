from datetime import datetime
print('='*8, 'ALISTAMENTO MILITAR', '='*8)
data_nasc = int(input('digite seu ano de nascimento: '))
data_atual = datetime.today().year
difer = data_atual - data_nasc
if difer == 18:
    print('Está na hora de se alistar!')
elif difer > 18:
    print("Você perdeu o prazo de alistamento, por favor procure o exercito brasileiros para informaçõs!"
          f"\nVocê deveria ter se alistado há {difer-18} ano(s)")
elif difer < 18:
    print('Ainda não está no prazo de alistamento'
          f'\nVocê deve se alistar daqui {18-difer} ano(s)!')