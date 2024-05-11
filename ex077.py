palavras = ('Abacate', 'Banana', 'Parto', 'Lapis', 'Encontar', 'Reinan')
for i in palavras:
    word = i.lower()
    contador = 0
    letras = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for l in letras:
        contador += word.lower().count(l)
    print(f'Em {i} existem {contador} vogais são elas: ', end=' ')
    for p in word:
        if p in 'aeiou':
            print(p, end='')
    print(' ')

