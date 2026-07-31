n = int(input("Enter a number: "))

i = 1
while i * i <= n:
    i += 1

root = i - 1

if root * root == n:
    if root < 2:
        print("Square root is not prime")
    else:
        prime = True
        for i in range(2, root):
            if root % i == 0:
                prime = False
                break

        if prime:
            print("Square root is prime")
        else:
            print("Square root is not prime")
else:
    print("Number is not a perfect square")
    