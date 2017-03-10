class Account():

    numberOfAccounts = 0
    accountLookup = dict()

    def __init__(self, name):
        self._accountName = name
        self._moneyInAccount = 0
        self._actID = Account.numberOfAccounts
        Account.numberOfAccounts += 1
        Account.accountLookup[self._actID] = self
        

if __name__ == '__main__': pass
