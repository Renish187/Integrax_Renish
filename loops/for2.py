# printing patterns like (Example of nested loop)
# *
# * *
# * * *
# * * * *

a=int(input("Enter a positive number:"))

for i in range(1,a+1):
    for j in range(1,i+1):
        print("* ",end='')
    print()
    