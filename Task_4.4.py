# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные 
# операции — функции. Дополнительно сохраняйте все операции поступления 
# и снятия средств в список.

MAX_SUM = 5_000_000
PERCENT = 1.015
BONUS = 1.03
TAX = 1.1
balance = 0
number_of_operations = 0
operations = []

def add_money():
    global balance
    while True:
        money = int(input('Введите сумму пополнения, кратную 50 у.е. '))
        if money % 50 == 0:
            balance += money
            break
        else:
            return 'Сумма пополнения не кратна 50 у.е.\n'
    operat(f'пополнение: {money}')
    balance = new_bonus(balance)
    return f'Вы пополнили счет на {money} у.е.\n\
Cумма на счете составляет {balance} у.е.\n'

def get_money():
    global balance
    if balance == 0:
        return 'На балансе нет средств\n'
    else:
        while True:
            money = int(input('Введите сумму снятия, кратную 50 у.е. '))
            if money % 50 == 0:
                fee = gift(money)
                if money + fee <= balance:
                    balance -= money + fee
                    break
                else:
                    return 'Недостаточно средств!\n'       
            else:
                return 'Сумма снятия не кратна 50 у.е.\n'
        operat(f'снятие: {money}')
        balance = new_bonus(balance)
        return f'Вы сняли со счета {money} у.е., комиссия - {fee} у.е.\n\
Остаток на счете составляет {balance} у.е.\n'
    
def gift(money):
    fee = money * PERCENT / 100
    if fee < 30:
        fee = 30
    elif fee > 600:
        fee = 600
    return fee

def new_bonus(balance):
    global number_of_operations
    if number_of_operations == 2:
        balance = balance * BONUS
        number_of_operations = 0
    else:
        number_of_operations += 1
    return balance

def wealth_tax(balance):
    if balance <= MAX_SUM:
        balance - balance * TAX
    return balance

def operat(tools: str):
    operations.append(tools)
    
while True:
    choise = input('Выберите действие:\n\
1 - пополнить\n\
2 - снять\n\
0 - выйти\n')
    match choise:
        case '1':
            wealth_tax(balance)
            print(add_money())     
        case '2':
            wealth_tax(balance)
            print(get_money())
        case '0':
            print('До свидания!')
            quit()

# Что считается ошибочной операцией?
