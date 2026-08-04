def encrypt(text, shift):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result += ch

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)