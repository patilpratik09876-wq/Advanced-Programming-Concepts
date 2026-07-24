num = int(input("Enter a number: "))

n = num
rev = 0

while num > 0:
    d = num % 10
    rev = rev * 10 + d
    num = num // 10

if n == rev:
    print("Palindrome")
else:
    print("Not Palindrome")
