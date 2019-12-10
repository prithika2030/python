class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome to our INDIAN BANK")
    def mail(self):
         email=input("Enter the email id:")
    def pas(self):
        while True:
        pin=input("Enter the password:")
        if(len(pin)>=8):
            print(pin)
            break
        else:
            print("Please enter the correct pin number")
            continue
    def userlogin(self):
        name=input("Enter the  username:")
        for i in name:
            if(ord(i) not in range(65,123)):
                print("Enter the correct name:")
                print(name)
    def mobile(self):
        while True:
        mob=input("Enter the mobile number")
        if(len(mob)>=10 and mob[0]=="9"):
            print(mob)
            break
        else:
            print("Please enter the correct mobile number")
            continue
    def accno(self):
        while True:
        num=input("Enter the account number:")
        if(len(num)>=12):
            print(num)
            break
        else:
            print("Enter the correct account number")
            continue
    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)
    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")
    def display(self):
        print("\n Net Available Balance=", self.balance)
s = Bank_Account()
s.userlogin()
s.mail()
s.pas()
s.mobile()
s.accno()
s.deposit()
s.withdraw()
s.display()

