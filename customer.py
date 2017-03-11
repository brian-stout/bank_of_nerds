from accounts.account import Account


class Customer():
    def __init__(self, firstName, lastName, age, userID):
        self._firstName = firstName
        self._lastName = lastName
        self._userID = userID
        self._userAge = age

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

    def __str__(self):
        return self._firstName + " " + self._lastName + " ID: " + str(self._userID)

    def add_account(self, account):
        self._accounts.append(account)

    def print_accounts(self):
        loopCount = 1
        for account in self.accounts:
            print(str(loopCount) + ". " + str(account))
            loopCount += 1


if __name__ == '__main__':
    pass
