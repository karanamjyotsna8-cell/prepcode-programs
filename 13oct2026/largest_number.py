num1=int(input("enter your number:"))
num2=int(input("enter your number:"))
num3=int(input("enter your number:"))
if num1>num2:
    if num1>num3:
        if num3>num2:
            print("largest numbe='num1'")
        else:
            print("largest number='num2'")
    else:
            print("largest number='num3'")
else:
            print("largest number='num1'")