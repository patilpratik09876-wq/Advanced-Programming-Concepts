s = input("Enter a string: ")

frequency = {}

for ch in s:
    if ch != " ":
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

values = list(frequency.values())
values.sort(reverse=True)

if len(values) < 2:
    print("Second most frequent character does not exist")
else:
    second = values[1]

    for ch in frequency:
        if frequency[ch] == second:
            print("Second most frequent character:", ch)
            print("Frequency:", second)
            break