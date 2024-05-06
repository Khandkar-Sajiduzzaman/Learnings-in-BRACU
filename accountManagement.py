class Account:
    count=0

    def __init__(self, name, age, occupation, amount):
        self.name=name
        self.age=age
        self.occoupation=occupation
        self.amount=amount
        Account.count+=1

    def addMoney(self, amount):
        self.amount+=amount

    def withdrawMoney(self, amount):
        if self.amount>=amount:
            self.amount-=amount
        else:
            print("Insufficient Balance")

    def printDetails(self):
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Occupation:  {self.occoupation}\n"
              f"Total Amount: {self.amount}")


print('No of account holders:', Account.count)
print("=========================")
p1 = Account("Abdul", 45, "Service Holder", 500000)
p1.addMoney(300000)
p1.printDetails()
print("=========================")
p2 = Account("Rahim", 55, "Businessman", 700000)
p2.withdrawMoney(700000)
p2.printDetails()
print("=========================")
p3 = Account("Ashraf", 62, "Govt. Officer", 200000)
p3.withdrawMoney(250000)
p3.printDetails()
print("=========================")
print('No of account holders:', Account.count)
