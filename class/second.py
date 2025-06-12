
class BankAccount:
    def __init__(self,acc,name,age):
        self.acc=acc
        self.name=name
        self.age = age
    
class SavingsAcc(BankAccount): #this is called single inheritance
    def __init__(self, acc, name, age,amount):
        super().__init__(acc, name, age)
        self.amount=amount
        

abc = SavingsAcc(4532359,"Renish",23,12345670)
print(abc.acc)
print(abc.name)
print(abc.age)
print(abc.amount)
if(abc.age >=18):
      print("Account is major.")
else:
       print("Account is minor.")
        