class BracuStudent:
    def __init__(self, name, home ):
        self.name=name
        self.home=home
        self.bus_pass=False

    def show_details(self):
        print(f"Student Name: {self.name}\n"
             f"Lives in {self.home}\n"
             f"Have Bus Pass? {self.bus_pass}")

    def get_pass(self):
        self.bus_pass=True

class BracuBus:
    def __init__(self, route, capacity=2):
        self.route=route
        self.capacity=capacity
        self.passenger_list=[]

    def show_details(self):
        print(f"Bus Route: {self.route}\n"
              f"Passengers Count: {len(self.passenger_list)} (Max: {self.capacity})\n"
              f"Passengers On Board: {self.passenger_list}")

    def board(self, *args):
        if len(args)==0:
            print("No passengers!")
        else:
            for i in args:
                if i.bus_pass==False:
                    print("You don't have a bus pass!")
                elif i.home!=self.route:
                    print("You got on the wrong bus!")
                else:
                    self.passenger_list+=[i.name]
                    if len(self.passenger_list)> self.capacity:
                        print(f"Bus is full!")
                        self.passenger_list.pop()
                    else:
                        print(f"{i.name} boarded the bus.")

st1 = BracuStudent("Afif", "Mirpur")
print("1===========================")
st2 = BracuStudent("Shanto", "Motijheel")
st3 = BracuStudent("Taskin", "Mirpur")
st1.show_details()
st2.show_details()
print("2===========================")
st3.show_details()
print("3===========================")
bus1 = BracuBus("Mirpur")
bus2 = BracuBus("Azimpur", 5)
bus1.show_details()
bus2.show_details()
print("4===========================")
st2.get_pass()
st3.get_pass()
print("5===========================")
st2.show_details()
st3.show_details()
print("6===========================")
bus1.board()
print("7===========================")
bus1.board(st1, st2)
print("8===========================")
st1.get_pass()
st2.home = "Mirpur"
st1.show_details()
st2.show_details()
print("9===========================")
bus1.board(st1, st2, st3)
print("10===========================")
bus1.show_details()
