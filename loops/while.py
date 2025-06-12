# Using while loop we will print multiplier table 
print("This is a multiplier table:")
i=1
while i <11:
    j=1
    while j < 11:
        print(i*j,"\t",end='')
        j+=1
    i+=1
    print()
