# Hollow square

a=int(input("Enter a positive integer:"))
if(a > 0):
    pass
else:
    print("You did not enter a positive integer.")
    exit()

for i in range(1,a+1):
    for j in range(1,a+1):
        if(i==1 or i==a or j==1 or j==a):
            print("* ",end='')
        else:
            print("  ",end='')
    print()    