frase = str(input('Digite um palíndromo: '))
frase = frase.lower().replace(' ', '')
fraseF = frase.replace(' ','').lower()
print(fraseF)
if frase == fraseF[::-1]:
    print('A frase é um palindromo!')
else: print('A frase não é um palindromo')
