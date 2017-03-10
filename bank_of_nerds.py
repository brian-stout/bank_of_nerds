#!usr/bin/env python3


#TODO: Make a bank teller class to see all the customers and accounts in
from bank import Bank
from customer import Customer

from accounts.savings import Savings
from accounts.checkings import Checkings
from accounts.retirement import Retirement

def print_bank_menu():
    print("A: Create customer")
    print("B: View all customers")
    print("C: View customer data by userID")
    print("D: Access customer accounts by userID")
    print("E: Access customer accounts by list")
    print("F: View all bank accounts")
    print("Q: Quit the program")

def print_customer_menu():
    print("A: View account balance")
    print("B: Deposit money to account")
    print("C: Withdraw money from account")
    print("D: Create a new account")

def create_customer(bank):

    firstName = input("Please enter your first name: ")
    lastName = input("Pleaase enter your last name: ")

    newCustomer = Customer(firstName, lastName, bank.numberOfCustomerIDs)

    #By default the bank creates a checkings and savings account
    newCustomer.accounts.append(create_account(bank, "Checkings", "Checkings Act"))
    newCustomer.accounts.append(create_account(bank, "Savings", "Savings Act")) 

    bank.add_customer(newCustomer)

def create_account(bank, actType, name):
    actID = bank.numberOfAccounts

    if actType == "Checkings":
        newAccount = Checkings(name, actID)
    elif actType == "Savings":
        newAccount = Savings(name, actID)
    elif actType == "Retirement":
        newAccount = Retirement(name, actID)

    bank.add_account(newAccount)

    return bank.accountLookup[actID]

#TODO: Add default option for key not found (Also empty dictionary)
def option_c(bank):
    userID = input("Please enter the user's ID number: ")
    userID = int(userID)

    #TODO: Will include all accounts later
    customer = bank.customer_lookup(userID)
    print(customer)

def option_d(bank):
    userID = input("Please enter the user's ID number: ")
    customer = bank.customer_lookup(int(userID))
    
    print("All of the user's accounts")
    if customer.print_accounts():
        customer.print_accounts()


    

def option_e():
    print("Option E")

def main():
    nerdBank = Bank()

    quit = False

    while(quit == False):
        print_bank_menu()

        while True:
            switch = input("\nSelect a menu option: ")

            if switch.upper() == "A":
                create_customer(nerdBank)
            elif switch.upper() == "B":
                nerdBank.view_customers()
            elif switch.upper() == "C":
                option_c(nerdBank)
            elif switch.upper() == "D":
                option_d(nerdBank)
            elif switch.upper() == "E":
                option_e()
            elif switch.upper() == "F":
                option_f()
            elif switch.upper() == "Q":
                quit = True
                break
            else:
                print("Please choose a valid menu option!")


if __name__ == '__main__':
    main()
