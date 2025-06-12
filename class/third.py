class Employee:
    company = "Integrax"
    def __init__(self,name,salary):
        self.name=name
        self.salary = salary
    def promotion(self):
        self.salary = self.salary + self.salary*10/100
        return self.salary
    
abc=Employee("Mahesh",120000)
print("Congratulations you are promoted, new salary is :",abc.promotion())

