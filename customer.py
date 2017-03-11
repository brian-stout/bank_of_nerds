from accounts.account import Account

"""
    Class handles maintaing data specifically about the customer's
        using the bank.  From a customer object you can reference all
        the account objects associated with him specifically for easy
        access, and to avoid allowing other customer objects to see
        bank specific information
"""


class Customer():
    def __init__(self, firstName, lastName, age, userID):
        self._firstName = firstName
        self._lastName = lastName
        self._userID = userID
        self._userAge = age

        # A list responsible for keeping track of all
        # the accounts the customer has
        self._accounts = list()

    @property
    def userID(self):
        return self._userID

    @property
    def accounts(self):
        return self._accounts

    @property
    def userAge(self):
        return self._userAge

    # EX:  Ricky Bobby ID: 0
    def __str__(self):
        return self._firstName + " " + self._lastName + " ID: " + str(self._userID)

    def add_account(self, account):
        self._accounts.append(account)

    # Used to print all the customer's accounts in a list
    # prefixed with numbers 1 through whatever
    def print_accounts(self):
        loopCount = 1
        for account in self.accounts:
            print(str(loopCount) + ". " + str(account))
            loopCount += 1


if __name__ == '__main__':
    pass
