from accounts.account import Account

class Customer():
    def __init__(self, firstName, lastName, userID):
        self._firstName = firstName
        self._lastName = lastName
        self._userID = userID

        self._accounts = list()

    @property
    def userID(self):
        return self._userID

    @property
    def accounts(self):
        return self._accounts

    def __str__(self):
        return self._firstName + " " + self._lastName + " ID: " + str(self._userID)

    def add_account(self, account):
        self._accounts.append(account)

    def print_accounts(self):
        for account in self.accounts:
            print(account)

if __name__ == '__main__': pass
