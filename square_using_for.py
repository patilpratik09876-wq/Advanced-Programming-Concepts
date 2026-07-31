n=int(input("Enter a natural number: "))
if n>0:
    print("Square numbers up to", n, "are:")
    for i in range(1, n+1):
        print(i**2)
else:
    print("Please enter a natural number.")