# class declaration

class Person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age =age


abc = Person(input("Enter your name:"),input("Enter your gender:"),input("Enter your age:"))
print(abc.name)
print(abc.gender)
print(abc.age)
