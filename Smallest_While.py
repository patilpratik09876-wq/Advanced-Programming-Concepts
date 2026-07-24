n = int(input("Enter how many numbers: "))

i = 1
smallest = int(input("Enter number: "))

while i < n:
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num
    i = i + 1

print(smallest)
