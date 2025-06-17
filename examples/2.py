# Solid square

a=int(input("Enter a positive integer:"))
if(a > 0):
    pass
else:
    print("You did not enter a positive integer.")
    exit()

for i in range(1,a+1):
    for j in range(1,a+1):
            print("* ",end='')    
    print()    