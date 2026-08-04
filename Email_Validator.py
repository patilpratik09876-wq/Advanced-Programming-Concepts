email = input("Enter email address: ")

if "@" in email and "." in email:
    at_position = email.index("@")
    dot_position = email.rfind(".")

    if (at_position > 0 and
        dot_position > at_position + 1 and
        dot_position < len(email) - 1):

        print("Valid email address")
    else:
        print("Invalid email address")
else:
    print("Invalid email address")