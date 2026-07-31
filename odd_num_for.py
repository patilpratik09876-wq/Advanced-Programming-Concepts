n=int(input("Enter a natural number: "))
if n>0:
    print("Odd numbers up to", n, "are:")
    for i in range(1, n+1):
        if i%2==1:
            print(i)
else:
    print("Please enter a natural number.")