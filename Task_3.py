k = 0

while True:
    number = int(input('Введите число: '))
    if number < 0:
        print('Число не должно быть отрицательным, повторите попытку!')
    elif number > 100000:
        print('Число не должно превышать 100000, повторите попытку!')
    else:
        break
if number == 0:
    print('Ноль - не натуральное число')
elif number == 1:
    print('Единица не относится к простым и составным числам')

for i in range(2, number // 2 + 1):
    if (number % i == 0):
        k += 1
if (k <= 0):
    print(f'{number} - простое число')
else:
    print(f'{number} - составное число')