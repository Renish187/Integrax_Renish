print("\nHello, let's calculate your BMI and calory burnt per day!")
print("\n Please enter some information:\n")
a=float(input("Weight in kgs:"))
b=float(input("Height in meters:"))
c=int(input("Age in years:"))
d=input("Male or Female:")
e=int(input("How many days a week do you exercise ?"))

bmi=(a/b**2)
print(bmi)
print("\n")
if(bmi<float(16)):
    print("Severe Thinness.")
elif(bmi>float(16) and bmi<18.5):
    print("Moderate Thinness.")
elif(bmi >18.5 and bmi < float(25)):
    print("Normal")
elif(bmi >float(25)):
    print("Overweight")

if (d=="Male"):
    bmr = 13.75*a +5*b -6.76*c +66
else:
    bmr =9.56*a + 1.85*b -4.68*c +655

if(e==0):
    bmr = bmr*1.2
elif(e<3):
    bmr = bmr * 1.375
elif (e<5):
    bmr = bmr*1.55
else:
    bmr *= 1.9

print("Calories burnt per day : ")
print(bmr)