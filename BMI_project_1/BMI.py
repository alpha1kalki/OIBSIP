# Body Mass Index Calculator

print("Welcome to BMI calculator")

weight = float(input("Enter your Weight in kg : "))
height = float (input("Enter your Height in meters :"))

BMI = weight / height ** 2

if BMI < 18.5:
    print("Under weight")

elif BMI < 25:
    print("Healthy weight")

else:
    print("Over Weight")    
