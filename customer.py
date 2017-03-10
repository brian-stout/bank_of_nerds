class Customer():

    numberOfCustomers = 0
    customerLookup = dict()

    def __init__(self, firstName, lastName):
        self._firstName = firstName
        self._lastName = lastName

        self._userID = Customer.numberOfCustomers
        Customer.numberOfCustomers += 1
        Customer.customerLookup[self._userID] = self

        self._checkingAccount = list()
        self._savingAccount = list()
        self._retirementAccount = list()

    def __str__(self):
        return self._firstName + " " + self._lastName + " ID: " + str(self._userID)

if __name__ == '__main__': pass
