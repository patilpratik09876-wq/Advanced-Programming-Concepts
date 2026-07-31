x = float(input("Enter x: "))
n = int(input("Enter n: "))

sum = 0
fact = 1
power = 1

for i in range(0, n + 1, 2):
    if i == 0:
        fact = 1
        power = 1
    else:
        fact = fact * (i - 1) * i
        power = power * x * x

    term = power / fact

    if (i // 2) % 2 == 0:
        sum = sum + term
    else:
        sum = sum - term

print("Cosine value =", sum)