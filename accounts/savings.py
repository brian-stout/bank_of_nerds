from accounts.account import Account

"""
    Savings account class is used to created
        account objects specifically for saving
        in the bank

    The only difference between a checkings account
        and a savings account is it keeps track of an
        interest, which is ultimately useless for this
        program
"""


class Savings(Account):

    def __init__(self, name, actID):
        super().__init__(name, actID)
        self._accountType = "Savings"
        self._interestRate = 0.0001

if __name__ == '__main__':
    pass
