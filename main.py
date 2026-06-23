class Employee:
    def __init__(self,name,salary):
        self.name:str = name
        self._salary: int = salary
    def intor(self):
        return f"my salary is {self.salary},and my name is {self.name}"

    @property
    def salary(self):
        return self._salary
    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError("Salary cannot be a negative value")
        self._salary = value
class Manager(Employee):
    def __init__(self, name, salary,team_count):
        super().__init__(name, salary)
        self.team_count = team_count
    def manager(self):
        return f"Hi i am {self.name}, I manage {self.team_count} people"
    



emp = Employee("Alex",2039)

print(emp.intor())
