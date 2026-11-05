from time import sleep
import emoji
print('Os fogos vão estourar em')
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print(emoji.emojize(':fireworks:' * 10))