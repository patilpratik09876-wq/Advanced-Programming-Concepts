n1=int(input("Enter a First Number:"))
n2=int(input("Enter a Second Number:"))
n3=int(input("Enter a Third Number:"))

if n1<n2 and n1<n3:
    print("The first number is smallest")
elif n2<n3 and n2<n1:
    print("The second number is smallest")
else:
    print("The third number is smallest")
