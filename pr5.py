# PR5 (OOP Wrapper)

class Person:
    def __init__(self):
        self.name = None
        self.age = None

    def setdata(self):
        self.name = input("Enter person name: ")
        self.age = int(input("Enter person age: "))

    def getdata(self):
        print(f"Person created with Name: {self.name}, Age: {self.age}")


class Employee:
    def __init__(self):
        self.name = None
        self.age = None
        self.ID = None
        self.salary = None

    def setdata(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.ID = int(input("Enter employee ID: "))
        self.salary = int(input("Enter salary: "))

    def getdata(self):
        print(f"Employee: Name: {self.name}, Age: {self.age}, ID: {self.ID}, Salary: {self.salary}")


class Manager:
    def __init__(self):
        self.name = None
        self.age = None
        self.ID = None
        self.salary = None
        self.department = None

    def setdata(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.ID = int(input("Enter manager ID: "))
        self.salary = int(input("Enter salary: "))
        self.department = input("Enter department: ")

    def getdata(self):
        print(f"Manager: Name: {self.name}, Age: {self.age}, ID: {self.ID}, Salary: {self.salary}, Department: {self.department}")


# Variables to hold instances
p1 = None
e1 = None
m1 = None

while True:
    print("\n--- Choose an Operation ---")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Compare Salaries")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    match choice:
        case 1:
            p1 = Person()
            p1.setdata()
            p1.getdata()

        case 2:
            e1 = Employee()
            e1.setdata()
            e1.getdata()

        case 3:
            m1 = Manager()
            m1.setdata()
            m1.getdata()

        case 4:
            print("\n--- Show Details ---")
            print("1. Person")
            print("2. Employee")
            print("3. Manager")
            print("4. Back to main menu")
            sub_choice = int(input("Enter your sub-choice: "))
            match sub_choice:
                case 1:
                    if p1:
                        p1.getdata()
                    else:
                        print("No person created yet.")
                case 2:
                    if e1:
                        e1.getdata()
                    else:
                        print("No employee created yet.")
                case 3:
                    if m1:
                        m1.getdata()
                    else:
                        print("No manager created yet.")
                case 4:
                    continue
                case _:
                    print("Invalid sub-choice!")

        case 5:
            if e1 and m1:
                if e1.salary > m1.salary:
                    print("Employee has a higher salary.")
                elif e1.salary < m1.salary:
                    print("Manager has a higher salary.")
                else:
                    print("Both have the same salary.")
            else:
                print("Please create both an employee and a manager first.")

        case 6:
            print("Exiting program. Thank you!")
            break

        case _:
            print("Invalid choice. Please select from 1 to 6.")







