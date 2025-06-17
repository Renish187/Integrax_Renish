# 8

for i in range(0,4):
    for j in range(0,4):
        if(i==00 or j==0 or j==3 or i==3):
            print(" *",end='')
        else:
            print("  ",end='')
    print()
for i in range(0,3):
    for j in range(0,4):
        if(j==0 or j==3 or i==2):
            print(" *",end='')
        else:
            print("  ",end='')
    print()