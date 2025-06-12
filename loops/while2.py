# To tell the prime numbers in the range given by the user

a=int(input("Enter a smaller number :"))
b=int(input("Enter a larger number :"))

if(a>b):
    a,b=b,a # This is used when the user makes error and enters reverse range like a=10 and b=5
# basically the above statement performs swapping

print("The prime numbers in range {0} to {1} is :".format(a,b))
# we can write above statement as print("The prime numbers in range " + a + " to " + b + " is :")
for i in range(a,b+1):
    j=1
    count =0
    while j<=i:
        if(i%j == 0):
            count +=1
        j+=1
    if(count <= 2):
        print(i,",",end='')
