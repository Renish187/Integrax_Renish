print("1- Add")
print("2- Sub")
print("3- Multiply")
print("4- Division")

option = int(input("Choose an operation:"))

l=[1,2,3,4]
if option in l:
    num1 = float(input("Enter first number :"))
    num2 = float(input("Enter second number :"))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif (option == 3):
        result = num1 * num2
    elif (option == 4 and num2!=0):
        result = num1 / num2
    if(num2==0 and option ==4):
        print("Second number is 0")
        result = 0
    print("your result is :{}".format(result))     
else:
    print("Invalid operation entered.")


