class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance
    def deposit(self,money):
        if money>0:
            self.balance += money
            print(f"Вы успешно пополнили свой счет. Сумма на счету - {self.balance}")

    def withdraw(self, money):
        if money>0 and money<=self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} с вашего счета. Сумма на счету - {self.balance}")
        else:
            print("Недостаточно средств на счету")
    def all_balance(self):
        print(f"Текущий баланс - {self.balance}")
man=Account("1",100)
man.deposit(50)
man.withdraw(30)
print(man.all_balance())