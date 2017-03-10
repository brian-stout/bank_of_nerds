class Account():

    def __init__(self, name, actID):
        self._accountName = name
        self._moneyInAccount = 0
        self._actID = actID
        self._accountType = "Default"

    @property
    def accountName(self):
        return self._accountName

    @property
    def accountType(self):
        return self._accountType

    @property
    def actID(self):
        return self._actID

    def deposit(self, money):
        if money > 0:
            self._moneyInAccount += money
        else:
            print("Error:  Can not add negative funds")

    def withdraw(self, money):
        if money > 0:
            if moneyInAccount > money:
                self._moneyInAccount -= money
            else:
                print("Overdraft detected!  There will be a 35$ Fee!")
                self._moneyInAccount -= (money + 35)
        else:
            print("Error: Can not withdraw negative funds")

    def __str__(self):
        return "\"" + self._accountName + "\" (" + self.accountType + ") Account ID: " + str(self._actID)
    
        

if __name__ == '__main__': pass
