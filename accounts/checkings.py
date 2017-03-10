from accounts.account import Account

class Checkings(Account):
    #TODO: Checkings account class identifier for customer print list?

    def __init__(self, name, actID):
        super().__init__(name, actID)
        self._accountType = "Checkings"

    #In an account I would like to
    #TODO: Print log history (Super?)
    #TODO: Add funds (Super)
    #TODO: Withdraw Money (Overdraft look on this)
    #TODO: Tansfer funds to another account

if __name__ == '__main__': pass
