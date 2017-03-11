"""
    The Account class handles the basic data for withdrawing
        and depositing to accounts, and used by retirement,
        checkings, and savings classes for most of their basic
        logic.
"""


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

    @property
    def moneyInAccount(self):
        return self._moneyInAccount

    def deposit(self, money):
        # Checking to avoid negative funds being added
        if money > 0:
            self._moneyInAccount += money
        else:
            print("Error:  Can not add negative funds")

    def withdraw(self, money, customer):
        # Checking to avoid negative funds from being added
        if money > 0:
            # Checks to see if withdrawing the money will
            # put the user in debt, and if it does
            # put them in debt and let them know they
            # triggered an over draft
            if self.moneyInAccount > money:
                self._moneyInAccount -= money
            else:
                print("Overdraft detected!  There will be a 35$ Fee!")
                self._moneyInAccount -= (money + 35)
        else:
            print("Error: Can not withdraw negative funds")

    def __str__(self):
        string = "\"" + self._accountName
        string = string + "\" (" + self.accountType + ") Account ID: "
        string = string + str(self._actID)
        return string


if __name__ == '__main__':
    pass
