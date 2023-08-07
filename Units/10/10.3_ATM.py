bank_account = {
    'balance': 1000.00
}


def check_balance():
    print(f"You have a balance of ${bank_account['balance']:.2f}")


def make_deposit():
    while True:
        deposit_amount = float(input("Enter the amount of money you want to deposit. To return to the option select menu, input '0'\n> "))
        if deposit_amount == 0:
            return False
        elif deposit_amount < 0:
            deposit_amount = float(input("You cannot deposit a negative amount. Please enter a positive amount to deposit. If you would like to return to the option select menu, input '0'\n> "))
            if deposit_amount == 0:
                return False
            elif deposit_amount > 0:
                bank_account['balance'] = bank_account['balance'] + deposit_amount
                print(f"{bank_account['balance']:.2f} Dollars successfully deposited your remaining balance is ${bank_account['balance']:.2f} ")
                print('')
                return False
            elif deposit_amount < 0:
                print("You cannot deposit a negative amount. Returning to option select menu\n")
                return False
        elif deposit_amount > 0:
            bank_account['balance'] = bank_account['balance'] + deposit_amount
            print(f"{bank_account['balance']:.2f} Dollars successfully deposited your remaining balance is ${bank_account['balance']:.2f} ")
            print('')
            return False


def make_withdraw():
    while True:
        cash_back = float(input("Enter the amount of money you want to withdraw. To withdraw nothing, input '0'\n> "))
        if cash_back == 0:
            return False
        elif cash_back > bank_account['balance']:
            print("You don't have sufficient balance to make this widthdrawal")
        else:
            bank_account['balance'] = bank_account['balance'] - cash_back
            print(f"{cash_back} Dollars successfully widthdrawn your remaining balance is {bank_account['balance']:.2f} Dollars")
            print('')
            return False


while True:

    prompt = input(f"Hello, welcome to the bank of Python \nCurrent balnce is ${bank_account['balance']:.2f} \nPlease choose an option: \n(B)alance \n(D)eposit \n(W)ithdraw \n(Q)uit \n> ")

    if prompt == 'B' or prompt == 'b':
        check_balance()
    elif prompt == 'D' or prompt == 'd':
        make_deposit()
    elif prompt == 'W' or prompt == 'w':
        make_withdraw()
    elif prompt == 'Q' or prompt == 'q':
        print("Thank you, come again!")
        break

''' Your assignment will be to write a Bank ATM program. Your ATM should allow the user to:

Check (B)alance
Make a (D)eposit
(W)ithdraw money
(Q)uit
You should create a function for each of the first three options above.

The program needs to keep running until the user decides to quit the program. '''
