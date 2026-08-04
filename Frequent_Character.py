s = input("Enter a string: ")

frequency = {}

for ch in s:
    if ch != " ":
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1

if len(frequency) > 0:
    most_frequent = ""
    highest = 0

    for ch in frequency:
        if frequency[ch] > highest:
            highest = frequency[ch]
            most_frequent = ch

    print("Most frequent character:", most_frequent)
    print("Frequency:", highest)
else:
    print("No characters found")