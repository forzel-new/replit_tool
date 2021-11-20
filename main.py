import requests as rq
import random
import string
import time

count = input('Кол-во ников: ')
symb = input('Кол-во символов: ')

nicks = []
time.sleep(1)
print('Начинаю генерацию ников...')
time.sleep(2)

def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    nicks.append(rand_string)
    print(f'[ GENERATED ] {rand_string}')

for i in range(int(count)):
	generate_random_string(int(symb))

print('Генерация ников завершена. Начинаю проверку ников через 3 секунды')
time.sleep(3)
print('Запущено. При обнаружении валида вы будете оповещены.')
for name in nicks:
    getcode = rq.get('http://replit.com/@' + str(name))
    if getcode.status_code in [404, '404']:
        pass
    else:
        print(f'https://replit.com/@{name} | Valid')
        with open('names.txt','a') as f:
            f.write(f'{name}\n')
        with open('names2.txt','a') as f:
            f.write(f'https://replit.com/@{name}\n')

print('Проверка завершена. Все валид коды были записаны в names.txt и names2.txt')
input()