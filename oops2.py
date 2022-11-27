# class Student:
#     def __init__(self,n,a,m):
#         self.name=n
#         self.age=a
#         self.marks=m
#     def display(self):
#         print("Name is ",self.name)
#         print("Age is ",self.age)
#         print("Marks is ",self.marks)
# s2=Student("Asad",19,90)
# s2.display()

# class Student:
#     def __init__(self,n,a,*m):
#         self.name=n
#         self.age=a
#         self.marks=m
#     def display(self):
#         print("Name is:- ",self.name)
#         print("Age is:- ",self.age)
#         print("Marks is:- ",self.marks)
# s2=Student("Asad",19,90,50,42) #add more than one marks because (*) before m
# s2.display()

# class Student:
#     def __init__(self,n,a,**m):
#         self.name=n
#         self.age=a
#         self.marks=m
#     def display(self):
#         print("Name is:- ",self.name)
#         print("Age is:- ",self.age)
#         print("Marks is:- ",self.marks)
# s2=Student("Asad",19,Eng=90,Math=50,ECE=42) #add more than one marks & subject name because (**) before m
# s2.display()
# print(type(s2.marks))

# class Student:
#     school_name = "ABC School"
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def change_school(cls,name):
#         print(Student.school_name)
#         Student.school_name = name
# jessa = Student('Jessa',14)
# Student.change_school("XYZ School")

# from datetime import date
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @classmethod
#     def calculate_age(cls,name,birth_year):
#         return cls(name,date.today().year - birth_year)
#     def show(self):
#         print(self.name+"'s age is: "+str(self.age))
# jessa=Student("Jessa",20)
# jessa.show()
# a = Student.calculate_age("Asad",2004)
# a.show()


class Employee:
    @staticmethod
    def sample(x):
        print("Inside static method",x)
Employee.sample(10)
emp=Employee()
emp.sample(20)


