class Student:
    total_student=0
    cse_student=0
    bba_student=0
    def __init__(self, name, department):
        self.name=name
        self.department=department
        Student.total_student+=1
        self.total_serial=Student.total_student
        if self.department== "CSE":
            Student.cse_student+=1
            self.department_serial= Student.cse_student

        else:
            Student.bba_student+=1
            self.department_serial= Student.bba_student

        print(f"Creating Student Number: {Student.total_student}")

    def individualInfo(self):
        print(f"{self.name} is from {self.department} department.\n"
              f"Serial of {self.name} among all students' is: {self.total_serial}\n"
              f"Serial of {self.name} in {self.department} department is: {self.department_serial}")

    def totalInfo(self):
        print(f"Total Number of Student: {Student.total_student}\n"
              f"Total Number of CSE Student: {Student.cse_student}\n"
              f"Total Number of BBA Student: {Student.bba_student}")


s1 = Student("Naruto", "CSE")
print('----------------------')
s1.individualInfo()
print('#############################')
s1.totalInfo()
print('============================')


s2 = Student("Sakura", "BBA")
print('----------------------')
s2.individualInfo()
print('#############################')
s2.totalInfo()
print('============================')


s3 = Student("Shikamaru", "CSE")
print('----------------------')
s3.individualInfo()
print('#############################')
s3.totalInfo()
print('============================')


s4 = Student("Deidara", "BBA")
print('----------------------')
s4.individualInfo()
print('#############################')
s4.totalInfo()