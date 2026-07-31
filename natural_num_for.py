n=int(input("Enter a natural number: "))
if n>0:
    print("Natural numbers up to", n, "are:")
    for i in range(1, n+1):
        print(i)
        