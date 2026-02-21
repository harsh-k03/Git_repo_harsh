class Person:
    
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello, I m {self.name}")

class Employee(Person):

    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    
    def introduce(self):
        super().introduce()
        print(f"I earn {self.salary}")
    
    def get_salary(self):
        return self.salary

class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def introduce(self):
        super().introduce()
        print(f"I code in {self.programming_language} ")
    
    def code(self):
        print(f"Coding in {self.programming_language}")

d = Developer("Alice", 5000,"python")  
d.introduce()
# print(d.get_salary())
# d.code()      


