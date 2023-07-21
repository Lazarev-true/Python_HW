# Возьмите 1-3 любые задачи из прошлых семинаров, которые вы уже решали. 
# Превратите функции в методы класса. Задачи должны решаться через вызов 
# методов экземпляра.

class BankAccount:
    MAX_SUM = 5_000_000
    PERCENT = 1.015
    BONUS = 1.03
    TAX = 1.1

    def __init__(self):
        self.balance = 0
        self.number_of_operations = 0
        self.operations = []

    def add_money(self):
        while True:
            money = int(input('Введите сумму пополнения, кратную 50 у.е. '))
            if money % 50 == 0:
                self.balance += money
                break
            else:
                return 'Сумма пополнения не кратна 50 у.е.\n'
        self.operat(f'пополнение: {money}')
        self.balance = self.new_bonus(self.balance)
        return f'Вы пополнили счет на {money} у.е.\n\
Cумма на счете составляет {self.balance} у.е.\n'

    def get_money(self):
        if self.balance == 0:
            return 'На балансе нет средств\n'
        else:
            while True:
                money = int(input('Введите сумму снятия, кратную 50 у.е. '))
                if money % 50 == 0:
                    fee = self.gift(money)
                    if money + fee <= self.balance:
                        self.balance -= money + fee
                        break
                    else:
                        return 'Недостаточно средств!\n'       
                else:
                    return 'Сумма снятия не кратна 50 у.е.\n'
            self.operat(f'снятие: {money}')
            self.balance = self.new_bonus(self.balance)
            return f'Вы сняли со счета {money} у.е., комиссия - {fee} у.е.\n\
Остаток на счете составляет {self.balance} у.е.\n'
    
    def gift(self, money):
        fee = money * self.PERCENT / 100
        if fee < 30:
            fee = 30
        elif fee > 600:
            fee = 600
        return fee

    def new_bonus(self, balance):
        if self.number_of_operations == 2:
            balance = balance * self.BONUS
            self.number_of_operations = 0
        else:
            self.number_of_operations += 1
        return balance

    def wealth_tax(self, balance):
        if balance <= self.MAX_SUM:
            balance - balance * self.TAX
        return balance

    def operat(self, tools: str):
        self.operations.append(tools)
    
    def run(self):
        while True:
            choise = input('Выберите действие:\n\
1 - пополнить\n\
2 - снять\n\
0 - выйти\n')
            if choise == '1':
                self.wealth_tax(self.balance)
                print(self.add_money())
            elif choise == '2':
                self.wealth_tax(self.balance)
                print(self.get_money())
            elif choise == '0':
                print('До свидания!')
                break

bank_account = BankAccount()
bank_account.run()
