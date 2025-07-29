num=int(input("Enter you number: "))
rev= 0

temp= num
while temp> 0:
    rem= temp%10
    rev= rem + (rev*10)
    temp= int(temp/10)

if rev==num:
    print("\nIt is a palindrome number.") 
else:       
    print("\nIt is NOT a palindrome number.")    