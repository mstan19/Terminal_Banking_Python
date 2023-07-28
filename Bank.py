import secrets
import sys
from os import system
class Bank:
    def __init__(self, name, id, saving, checking):
        self.name = name
        self.id = id
        self.saving = saving
        self.checking = checking
    
    def deposit_saving(self,adding_money):
        self.saving += adding_money
        print(f"Thank you for depositing money to your savings account. Your current balance is $ {self.saving}")
    
    def deposit_checking(self,adding_money):
        self.checking += adding_money
        print(f"Thank you for depositing money to your checking account. Your current balance is $ {self.checking}")
    
    def withdraw_saving(self,taking_out_money):
        if taking_out_money > self.saving:
            print(f"sorry, but you are broke. Your current balance is $ {self.saving}")
        else:
            self.saving -= taking_out_money
            print(f"Thank you for withdrawing money to your checking account. Your current balance is $ {self.saving}")
    
    def withdraw_checking(self,taking_out_money):
        if taking_out_money > self.checking:
            print(f"sorry, but you are broke. Your current balance is $ {self.checking}")
        else:
            self.checking -= taking_out_money
            print(f"Thank you for withdrawing money to your checking account. Your current balance is $ {self.checking}")
            
    def account_info(self):
        print(f"Owner: {self.name}")
        print(f"Account id: {self.id}")
        print(f"Saving Account Current balance: ${self.saving}")
        print(f"Checking Account Current balance: ${self.checking}")
        

# MENU OPTIONS
def main():
    # create an empty list to store accounts
    # array of objects
  accounts = []
# the current account that you selected

  while True:
    # display the menu of options
    print("-------------------------------------------------------------------")
    print("1. Create an account")
    print("2. Enter account id")
    print("3. Quit")
    print("-------------------------------------------------------------------")
    choice = int(input("Enter your choice: "))
   
    
    current_account = None
    
    def create_account():
        name = input("Enter your name: ")
        saving = float(input("How much money are you putting in your saving account? $"))
        checking = float(input("How much money are you putting in your checking account? $"))
        id = 10 + secrets.randbelow(500)
        bank = Bank(name, id, saving, checking)
        print(f"Your bank account ID: " + str(id))
        return bank
    
    def select_account(account_number):
        for account in accounts:
            if account.id == account_number:
                return account

    if choice == 1:
      # create a new account
        accounts.append(create_account())
    elif choice == 2:
      # Withdraw money from saving account
        account_number = int(input("Please enter your account number: "))
        current_account = select_account(account_number)
        print("print from choice " + str(current_account.id))
        while True:
            # subchoices
            print("-------------------------------------------------------------------")
            print("1. Withdraw money from saving account")
            print("2. Withdraw money from checking account")
            print("3. Deposit money from saving account")
            print("4. Deposit money from checking account")
            print("5. Check Over Balances")
            print("-------------------------------------------------------------------")
            sub_choices = int(input("Enter your choice: "))
            if sub_choices == 1:
            # Withdraw money from saving account
                withdrawl_amount = float(input("Please enter how much money you want to withdraw from your saving account: $ "))
                current_account.withdraw_saving(withdrawl_amount)
            elif sub_choices == 2:
            # Withdraw money from checking account
                withdrawl_amount = float(input("Please enter how much money you want to withdraw from your checking account: $ "))
                current_account.withdraw_checking(withdrawl_amount)
            elif sub_choices == 3:
            # Deposit money from saving account
                deposit_amount = float(input("Please enter how much money you want to deposit from your saving account: $ "))
                current_account.deposit_saving(deposit_amount)
            elif sub_choices == 4:
            # Deposit money from checking account
                deposit_amount = float(input("Please enter how much money you want to deposit from your checking account: $ "))
                current_account.deposit_checking(deposit_amount)
            elif sub_choices == 5:
            # Deposit money from checking account
                current_account.account_info()
            else:
                print("Invalid choice! Please try again.")
                break
    elif choice == 3:
      # exit the app
      break
    else:
      print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

    