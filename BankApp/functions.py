from Classes import *

runing = 1

def chooseWhoYouAre():
    print("Who are you? ")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")
    userInput = int(input("What is your choice: "))
    return userInput

def initital_display(user_type=None):
    print("*____________________________*")
    if user_type == None:
          print("Hello Welcome to Salem Bank")
          type = chooseWhoYouAre() 
    else:
        if type == 1:
            print(f"Hello{user_type} Welcome!")
            running = True
            while running == True:
                  CustomerDisplay()
        elif type == 2:
            adminDisplay()
        else:
            running == False 


def CustomerDisplay():
    print("Hello Customer, Welcome to Salem Bank")
    print("Please select an option from the menu below")
    print("1. SignUp")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Balance")
    print("5. Delete Account")
    print("6. Exit")
    userInput = int(input("What are you doing Today: "))
    if userInput == 1:
            SignUp()
    elif userInput == 2:
            DepositMoney()
    elif userInput== 3:
            WithdrawMoney()
    elif userInput== 4:
            RetrieveBalance
    elif userInput == 5:
            DeleteAccount()
    elif userInput == 6:
            Exit(runing,False)
    

def adminDisplay():
    print("Hello Admin, Welcome to CinemaHouseX2")
    print("Please select an option from the menu below")
    print("1. Display all Accounts")
    print("2. Display all Customers")
    print("3. Display all Employees ")
    userInput = int(input("What are you doing today: "))
    if userInput == 1:
        RetriveAccounts()
    elif userInput == 2:
        RetrieveCustomers()
    elif userInput == 3:
        RetrieveEmployees()
    


def SignUp():
      pass

def RetriveAccounts():
     pass
def RetrieveCustomers():
     pass
def RetrieveEmployees():
     pass
def DepositMoney():
     pass
def WithdrawMoney():
     pass
def RetrieveBalance():
     pass
def DeleteAccount():
     pass


def Exit(var,value):
     var = value 
     return var






    
