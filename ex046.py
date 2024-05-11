from time import sleep
import emoji
print('='*8, "CONTAGEM REGRESSIVA", '='*8)
for i in range(10,0, -1):
    print(i)
    sleep(1)
print(emoji.emojize(':fireworks:'))