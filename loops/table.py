# We are trying to print the table of the number entered by the user

a=int(input("Enter a number :"))

for i in range(1,11):
    print("{1} * {0} = {2}".format(i,a,a*i))
    