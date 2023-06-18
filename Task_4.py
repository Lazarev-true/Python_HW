from random import randint

n = 10
LOWER_LIMIT = 0
UPPER_LIMIT = 1000

num = randint(LOWER_LIMIT, UPPER_LIMIT)

while True:
    if n == 0:
        print('Попыток больше нет')
        break

    number = int(input(f'Угадайте число, у вас {n} попыток '))

    if number < 0 or number > 1000:
        print(f'Загадано число от {LOWER_LIMIT} до {UPPER_LIMIT}, введите заново')
    else:
        if number < num:
            print('Загаданное число больше')
            n -= 1
        elif number > num:
            print('Загаданное число меньше')
            n -= 1
        else:
            print('Вы угадали, поздравляю!')
            break