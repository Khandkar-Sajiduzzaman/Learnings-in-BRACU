class NikeBangladesh:
    branches=[]
    total_stock={'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
    total_sold=0
    @classmethod
    def status(cls):
        print(f"Nike Bangladesh Status:\n"
              f"Branches Opened: {cls.branches}\n"
              f"Currently Stocked {cls.total_stock}\n"
              f"Sold: {cls.total_sold} ")
    def __init__(self, branch):
        self.branch=branch
        self.sold=0
        self.stock={'Air Jordan': 0, 'Cortez': 0, 'Zoom Kobe': 0}
        NikeBangladesh.branches+=[self.branch]
    def details(self):
         print(f"Nike {self.branch} outlet: \n"
              f"Products Currently Stocked: {self.stock}\n"
              f"Sold: {self.sold}")
    def restockProducts(self, products):
        for k,v in products.items():
            self.stock[k]+=v
            NikeBangladesh.total_stock[k]+=v
    def productSold(self, products):
        for k,v in products.items():
            self.stock[k]-=v
            NikeBangladesh.total_stock[k]-=v
            self.sold+=v
            NikeBangladesh.total_sold+=v

print("xxxxxxxxxxxxxx1xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
dhaka = NikeBangladesh("Dhaka Banani")
chittagong = NikeBangladesh("Chittagong GEC")
print("xxxxxxxxxxxxxx2xxxxxxxxxxxxxxxx")
dhaka.details()
print("xxxxxxxxxxxxxx3xxxxxxxxxxxxxxxx")
chittagong.details()
print("xxxxxxxxxxxxxx4xxxxxxxxxxxxxxxx")
dhaka.restockProducts({"Air Jordan":1200,"Cortez":200,"Zoom Kobe":200})
chittagong.restockProducts(
{"Air Jordan":1000,"Cortez":250,"Zoom Kobe":100})
print("xxxxxxxxxxxxxx5xxxxxxxxxxxxxxxx")
NikeBangladesh.status()
print("xxxxxxxxxxxxxx6xxxxxxxxxxxxxxxx")
dhaka.productSold({"Air Jordan":760,"Cortez":90})
chittagong.productSold({"Air Jordan":520,"Zoom Kobe":70})
print("xxxxxxxxxxxxxx7xxxxxxxxxxxxxxxx")
NikeBangladesh.status()