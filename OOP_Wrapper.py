class Emp:
    def __init__(self, empId, name, age, salary):
        self.empId = empId
        self.name = name
        self.age = age
        self.salary = salary
    def getInfo(self):
        print(f"ID:{self.empId}, Name:{self.name}, Age:{self.age}, Salary:{self.salary}")


class Manager(Emp):
    def __init__(self, empId, name, age, salary, department):
        super().__init__(empId, name, age, salary)
        self.department = department

    def getInfo(self):
        print(f"ID:{self.empId}, Name:{self.name}, Age:{self.age}, Salary:{self.salary}, Department: {self.department}")


class Developer(Emp):
    def __init__(self, empId, name, age, salary, programming_language):
        super().__init__(empId, name, age, salary)
        self.programming_language = programming_language

    def getInfo(self):
        print(f"ID:{self.empId}, Name:{self.name}, Age:{self.age}, Salary:{self.salary}, Programming Language: {self.programming_language}")

obj = None
employees = []
print("--- Python OOP Project : Employee Management System ---")
while True:
    print("Enter 1 to Create Employee")
    print("Enter 2 to Create Manager")
    print("Enter 3 to Create Developer")
    print("Enter 4 to View Information")
    print("Enter 5 to Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        empId = input("Enter ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = int(input("Enter salary: "))
        obj = Emp(empId, name, age, salary)
        employees.append(obj)
    elif choice == 2:
        empId = input("Enter ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = int(input("Enter salary: "))
        department = input("Enter department: ")
        obj = Manager(empId, name, age, salary, department)
        employees.append(obj)
    elif choice == 3:
        empId = input("Enter ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        salary = int(input("Enter salary: "))
        programming_language = input("Enter programming language: ")
        obj = Developer(empId, name, age, salary, programming_language)
        employees.append(obj)
    elif choice == 4:
        choice_info = int(input("\n1 To view Employee, \n2 To view Manager, \n3 To view Developer: "))
        if choice_info == 1:
            if employees:
                print("Employee Information:")
                for emp in employees:
                    if isinstance(emp, Emp):
                        emp.getInfo()
            else:
                print("No employee created.")
        elif choice_info == 2:
            if employees:
                print("Manager Information:")
                for emp in employees:
                    if isinstance(emp, Manager):
                        emp.getInfo()
            else:
                print("No manager created.")
        elif choice_info == 3:  
            if employees:
                print("Developer Information:")
                for emp in employees:
                    if isinstance(emp, Developer):
                        emp.getInfo()
            else:
                print("No developer created.")
    elif choice == 5:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice")
