class Calculator:

    def __init__(self,n):
        self.n=n
    def Square(self):
     return self.n**2
    def Cube(self):
       return self.n **3
    def Squareroot(self):
       return self.n**(1/2)

abc=Calculator(12)
print("The cube is :",abc.Cube())
print("The Square is :",abc.Square())
print("The Square Root is :",abc.Squareroot())
