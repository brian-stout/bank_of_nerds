class Customer():

    numberOfCustomers = 0
    customerList = dict()

    def __init__(self, firstName, lastName):
        self._firstName = firstName
        self._lastName = lastName

        self._userID = Customer.numberOfCustomers
        Customer.numberOfCustomers += 1

        self._checkingAccount = list()
        self._savingAccount = list()
        self._retirementAccount = list()

if __name__ == '__main__': pass
