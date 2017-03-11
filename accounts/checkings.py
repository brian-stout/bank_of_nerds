from accounts.account import Account


class Checkings(Account):

    def __init__(self, name, actID):
        super().__init__(name, actID)
        self._accountType = "Checkings"


if __name__ == '__main__':
    pass
