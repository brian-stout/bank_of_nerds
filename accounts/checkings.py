from accounts.account import Account

"""
    The checkings account handles most of the base logic for the most
        basic of bank accounts.  Doesn't do anything special compared
        to the retirement account or savings account (if interested was
        being handled)
"""


class Checkings(Account):

    def __init__(self, name, actID):
        super().__init__(name, actID)
        self._accountType = "Checkings"


if __name__ == '__main__':
    pass
