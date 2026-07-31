s = input("Enter a string: ")

duplicates = ""

for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] == s[j] and s[i] not in duplicates:
            duplicates += s[i]

print("Duplicate characters:", duplicates)