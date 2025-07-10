class Student:
    def __init__(self):
        self.__name = ""
        self.__marks = 0
    def set_name(self,name):
        self.__name = name
    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Error: Marks should be between 0 and 100.")
    def get_name(self):
        return self.__name
    def get_marks(self):
        return self.__marks
s=Student()
s.set_name("Hemanth")
s.set_marks(100)
print("Student Name:",s.get_name())
print("Student Marks:",s.get_marks())
s.set_marks(120)
print("Student Marks (after invalid input):",s.get_marks())