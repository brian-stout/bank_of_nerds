class Customer():

    numberOfCustomers = 0

    def __init__(self, firstName, lastName, moneyInPocket):
        self._firstName = firstName
        self._lastName = lastName
        self._moneyInPocket

        self._userID = Customer.numberOfCustomers
        Customer.numberOfCustomers += 1

        self._checkingAccounts = list()
        self._savingAccounts = list()
        self._retirementAccounts = list()

if __name__ == '__main__': pass
