from accounts.account import Account

class Retirement(Account):

    def __init__(self, name, actID):
        super().__init__(name, actID)
        self._accountType = "Retirement"

if __name__ == '__main__': pass
