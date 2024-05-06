class SultansDine:
    branch_number=0
    total_sell=0
    branch_list=[]

    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {cls.branch_number}\n"
             f"Total Sell: {cls.total_sell} Taka")
        for i in cls.branch_list:
            print(f"Branch Name: {i.branch}, Branch Sell: {i.branch_sell} Taka\n"
                  f"Branch consists of total sell's: {((i.branch_sell/cls.total_sell)*100):.2f}%")

    def __init__(self, branch):
        self.branch=branch
        self.branch_sell=0
        SultansDine.branch_list+=[self]
        SultansDine.branch_number+=1

    def sellQuantity(self, quantity):
        if quantity<10:
            self.branch_sell+= quantity*300
        elif quantity<20:
            self.branch_sell+= quantity*350
        else:
            self.branch_sell+= quantity*400
        SultansDine.total_sell+=self.branch_sell
    def branchInformation(self):
        print(f"Branch Name: {self.branch}\n"
              f"Branch Sell: {self.branch_sell} Taka")

SultansDine.details()
print('########################')
dhanmondi = SultansDine('Dhanmondi')
dhanmondi.sellQuantity(25)
dhanmondi.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()

print('========================')

gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()
