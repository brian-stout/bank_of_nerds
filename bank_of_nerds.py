#!usr/bin/env python3

from menus import *
from bank import Bank


def main():
    # Creates the bank
    nerdBank = Bank()

    quit = False

    # Only quits when user selects Q as the menu option
    while(quit is False):
        # A is to create new customer
        # B is to view all customers
        # C is to view the customer's data via ID
        # D is to access the customer's accounts via user ID, then menu options
        print_bank_menu()

        # Break after each options beside, default to print menu again
        while True:
            switch = input("\nSelect a menu option: ")

            if switch.upper() == "A":
                create_customer(nerdBank)
                break
            elif switch.upper() == "B":
                nerdBank.view_customers()
                break
            elif switch.upper() == "C":
                view_customer_data(nerdBank)
                break
            elif switch.upper() == "D":
                access_user_accounts(nerdBank)
                break
            elif switch.upper() == "Q":
                quit = True
                break
            else:
                # If all the conditionals failed
                # the user failed to provide good input
                print("Please choose a valid menu option!")

if __name__ == '__main__':
    main()
