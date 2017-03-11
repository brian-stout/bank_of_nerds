#!usr/bin/env python3

from menus import *
from bank import Bank


def main():
    nerdBank = Bank()

    quit = False

    while(quit is False):
        print_bank_menu()

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
                print("Please choose a valid menu option!")

if __name__ == '__main__':
    main()
