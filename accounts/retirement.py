from accounts.account import Account

"""
    Class is an account child class specifically for handling
        retirement accounts.  The only difference between the
        main account class and this, is the age restriction
        on withdrawing   
"""


class Retirement(Account):

    def __init__(self, name, actID):
        super().__init__(name, actID)
        self._accountType = "Retirement"

    def withdraw(self, money, customer):
        if customer.userAge >= 67:
            super().withdraw(money, customer)
        else:
            print("User too old to access retirement account!")


if __name__ == '__main__':
    pass
