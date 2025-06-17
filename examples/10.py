# heart making

for i in range(0,1):
    for j in range(0,10):
        if(j==2 or j==7):
            print(" *",end='')
        else:
            print(" ",end='')
    print()

for i in range(0,1):
    for j in range(0,10):
        if(j==0 or j==4 or j==9):
            print(" *",end='')
        else:
            print(" ",end='')
    print()

for i in range(0,6):
    for j in range(0,i+1):
        if(j==i):
            print(" *",end='')
        else:
            print(" ",end='')
    for j in range(i,5):
        print(" ",end='')
    for j in range(5,i,-1):
        print(" ",end='')
    for j in range(i,5):
        if(j==i):
            print("*",end='')
    print()