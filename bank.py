from customer import Customer

class Bank():
    def __init__(self):
        self._accountLookup = dict()
        self._numberOfAccounts = 0
        self._customerLookup = dict()
        self._numberOfCustomerIDs = 0

    @property
    def numberOfAccounts(self):
        return self._numberOfAccounts

    @property
    def numberOfCustomerIDs(self):
        return self._numberOfCustomerIDs

    @property
    def customerLookup(self):
        return self._customerLookup

    @property
    def accountLookup(self):
        return self._accountLookup

    def add_customer(self, newCustomer):
        self._customerLookup[newCustomer.userID] = newCustomer
        self._numberOfCustomerIDs += 1

    def add_account(self, newAccount):
        self._accountLookup[newAccount.actID] = newAccount
        self._numberOfAccounts += 1

    #TODO: Check for empty dictionaries
    def view_customers(self):
        if self.customerLookup:
            for customer in self.customerLookup:
                print(self.customerLookup[customer])
        else:
            print("There are no customers")  

    def customer_lookup(self, userID):
        return self._customerLookup.get(userID)
        
        
if __name__ == '__main__': pass
