class Student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def Details(self):
        return "Name: "+self.name+"\n"+"ID: "+self.ID+"\n"

class CSEStudent(Student):
    def __init__(self,name, ID, semester ):
        super().__init__(name,ID)
        self.semester=semester
        self.course_details={}

    def Details(self):
        return f"{super().Details()} current semester: {self.semester}"

    def addCourseWithMarks(self, *args):
        for i in range(0,(len(args)), 2):
            self.course_details[args[i]]=args[i+1]

    def showGPA(self):
        sum=00
        print(f"Bob has taken {len(self.course_details.keys())} courses")
        for k,v in self.course_details.items():
            if v>=85:
                v=4.00
            elif v>=80:
                v=3.3
            elif v>= 70:
                v=3.0
            elif v>= 65:
                v= 2.3
            elif v>=57:
                v=2.00
            elif v>=55:
                v=1.3
            elif v>=50:
                v=1.00
            else:
                v=0.00
            self.course_details[k]=v
            sum+=v
            print(f"{k}:{v}")
        print(f"GPA of Bob is: {sum/len(self.course_details.keys()): .2f}")

class Student:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def Details(self):
        return "Name: "+self.name+"\n"+"ID: "+self.ID+"\n"
#Write your code here

Bob = CSEStudent("Bob","20301018","Fall 2020")
Carol = CSEStudent("Carol","16301814","Fall 2020")
Anny = CSEStudent("Anny","18201234","Fall 2020")
print("#########################")
print(Bob.Details())
print("#########################")
print(Carol.Details())
print("#########################")
print(Anny.Details())
print("#########################")
Bob.addCourseWithMarks("CSE111",83.5,"CSE230",73.0,"CSE260",92.5)
Carol.addCourseWithMarks("CSE470",62.5,"CSE422",69.0,"CSE460",76.5,"CSE461",87.0)
Anny.addCourseWithMarks("CSE340",45.5,"CSE321",95.0,"CSE370",91.0)
print("----------------------------")
Bob.showGPA()
print("----------------------------")
Carol.showGPA()
print("----------------------------")
Anny.showGPA()