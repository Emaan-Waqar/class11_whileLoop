number= int(input("Enter you number: "))
digits= 0

while number != 0:
    digits= digits + 1
    number= number//10
print("You number has", digits,"digits")    