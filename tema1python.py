class Employee:
    """Common base class for all employees"""
    empCount = 0

#
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        """Displays the number of employees"""
        print(f"Total number of employee(s) is {Employee.empCount}")

    def display_employee(self):
        """Displays employee details"""
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__(self):
        Employee.empCount -= 1

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Tasks with status {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


    """Manager class inheriting from Employee"""

class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"B03_{department}"
        Manager.mgr_count += 1

    def display_employee(self):
        x = 10 % 3  
        if x == 0:
            print(f"Name: {self.name}")
        if x == 1:
            print(f"Salary: {self.salary}")
        if x == 2:
            print(f"Department: {self.department}")

#main.py

mgr1 = Manager("Tudorancea Marina-Andreea", 70000, "Marketing")
mgr2 = Manager("Stan Ioana", 2000, "IT")
mgr3 = Manager("Pavel Andrei", 1000, "IT")
mgr4 = Manager("Ion Maria", 3500 ,"Banking")


emp = Employee("Gavrila Diana", 30000)



print("Displaying  employees:")
emp.display_employee()

print("Displaying all managers:")
mgr1.display_employee()
mgr2.display_employee()
mgr3.display_employee()
mgr4.display_employee()

# Displaying counts of employees and managers
print(f"Employee count: {emp.empCount}")
print(f"Manager count: {mgr1.mgr_count}")