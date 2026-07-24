n = int(input("Enter the value of n: "))

count = 0
odd = 2
sum = 0

while count < n:
    sum += odd
    odd += 1
    count += 1

print("Sum of first", n, "odd numbers is:", sum)
