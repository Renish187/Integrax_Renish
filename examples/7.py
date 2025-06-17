# K making

for i in range(0,9):
    for j in range(i,9):
        if(j==i or j==8):
            print("*",end='')
        else:
            print(" ",end='')
    print()

for i in range(0,9):
    for j in range(0,i+1):
        if(j==0 or j==i):
            print("*",end='')
        else:
            print(" ",end='')
    print()