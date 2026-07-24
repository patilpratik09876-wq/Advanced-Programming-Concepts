n = int(input("Enter how many numbers: "))

i = 1
largest = int(input("Enter number: "))

while i < n:
    num = int(input("Enter number: "))
    if num > largest:
        largest = num
    i = i + 1

print(largest)
