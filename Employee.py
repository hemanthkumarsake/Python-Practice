class Employee:
    def __init__(self):
        self.__name = ""
        self.__salary = 0
        self.__age = 0
    def set_name(self,name):
        self.__name = name
    def set_salary(self,salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Error: Salary must be greater than 0.")
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary

    def set_age(self, age):
        if 18 <= age <= 100:
            self.__age = age
        else:
            print("Error: Age must be between 18 and 100.")
    def get_age(self):
        return self.__age
s=Employee()
s.set_name("Hemanth")
s.set_salary(10000000)
s.set_age(21)
print("Employee Name:",s.get_name())
print("Employee Salary:",s.get_salary())
print("Employee Age:",s.get_age())
s.set_salary(0)