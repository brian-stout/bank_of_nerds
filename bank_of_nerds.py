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

def print_account_menu():
    print("A: Deposit money to account")
    print("B: Withdraw money from account")
    print("C: Transfer money to another account")

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
def view_customer_data(bank):
    userID = input("Please enter the user's ID number: ")
    userID = int(userID)

    #TODO: Will include all accounts later
    customer = bank.customer_lookup(userID)
    print(customer)

def access_user_accounts(bank):
    userID = input("Please enter the user's ID number: ")
    customer = bank.customer_lookup(int(userID))
    
    print("All of the user's accounts")
    customer.print_accounts()

    print("Input a number to access an account")
    print("A. Create a new account")
    print("Q. Main menu")

    while True:
        switch = input("Choose an option: ")

        if switch.isdigit():
            userAccount = customer.accounts[int(switch) - 1]
            access_accounts(bank, customer, userAccount)
            break

        elif switch.upper() == "A":
            print("

            break

        elif switch.upper() == "Q":

            break

        else:
            print("Not a valid option")


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
                view_customer_data(nerdBank)
            elif switch.upper() == "D":
                access_user_accounts(nerdBank)
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
