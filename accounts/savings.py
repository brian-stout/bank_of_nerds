from accounts.account import Account

class Savings(Account):

    def __init__(self, name, actID):
        super().__init__(name, actID)
        self._accountType = "Savings"

if __name__ == '__main__': pass
