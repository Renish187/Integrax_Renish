
class Pattern:
    def __init__(self,n):
        self.n=n
    def Square(self):
        for i in range(1,self.n+1):
            j=1
            for j in range (1,self.n+1):
                if(i==1 or i==self.n or j==1 or j==self.n):
                    print("* ",end='')
                else:
                    print("  ",end='')
            print()

abc=Pattern(5)
abc.Square()