from random import randint
c=menor=maior=0
tupla = (randint(1,5), randint(1,5), randint(1,5),randint(1,5),randint(1,5))
print('Os números gerados foram:', end = " ")
print(f'''
O menor valor armazenado foi: {min(tupla)}
E o maior foi: {max(tupla)}''')


