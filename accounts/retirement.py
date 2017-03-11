from accounts.account import Account

class Retirement(Account):

    def __init__(self, name, actID):
        super().__init__(name, actID)
        self._accountType = "Retirement"

    def withdraw(self, money, customer):
        if customer.userAge >= 67:
            super().withdraw(money, customer)
        else:
            print("User too old to access retirement account!")
        

if __name__ == '__main__': pass
