# I

for i in range(0,7):
    for j in range(0,7):
        if(i==0 or i==6 or j==3):
            print(" *",end='')
        else:
            print("  ",end='')
    print()