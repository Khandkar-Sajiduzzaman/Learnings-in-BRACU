class Account:
    count = 0

    def __init__(self, name: str, age: int, occupation: str, balance: float):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.balance = balance
        Account.count += 1

    def add_money(self, amount: float) -> None:
        self.balance += amount

    def withdraw_money(self, amount: float) -> str:
        if self.balance >= amount:
            self.balance -= amount
            return "Withdrawal successful"
        else:
            return "Insufficient balance"

    def get_details(self) -> str:
        return (f"Name: {self.name}\n"
                f"Age: {self.age}\n"
                f"Occupation: {self.occupation}\n"
                f"Total Balance: {self.balance:.2f}")

    @staticmethod
    def get_account_count() -> int:
        return Account.count

# Testing the code
p1 = Account("Abdul", 45, "Service Holder", 500000)
p1.add_money(300000)
print(p1.get_details())
print("=========================")
p2 = Account("Rahim", 55, "Businessman", 700000)
print(p2.withdraw_money(700000))
print(p2.get_details())
print("=========================")
p3 = Account("Ashraf", 62, "Govt. Officer", 200000)
print(p3.withdraw_money(250000))
print(p3.get_details())
print("=========================")
print('No of account holders:', Account.get_account_count())
