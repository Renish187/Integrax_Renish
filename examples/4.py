# Hollow diamond

a=int(input("Enter a positive integer:"))
if(a > 0):
    pass
else:
    print("You did not enter a positive integer.")
    exit()

for i in range(1,a):
    for j in range(a,i,-1):
        print("*",end='')
    for j in range(1,i+1):
         print("  ",end='')
    for j in range(a,i,-1):
         print("*",end='')
    print()
for i in range(1,a):
    for j in range(1,i+1):
        print("*",end='')
    for j in range(a-1,i-1,-1):
        print("  ",end='')
    for j in range(1,i+1):
        print("*",end='')
    print()
