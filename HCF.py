num1= float(input("Enter number 1: "))
num2= float(input("Enter number 2: "))

while num2!=0:
    temp= num2
    num2 = num1 % num2
    num1 = temp

HCF= num1
print("Hcf is =", HCF)    