maritial_status=input("Enter maritial status(Married/Unmarried):").lower()
gender=input("Enter the Gender(Male/Female)").lower()
age=int(input("Enter a age:"))

if maritial_status=="married":
    print("The status will be insuerd")
elif maritial_status=="mnmarried":
    if gender=="male" and age>30:
        print("This will be insured")
    elif gender=="female" and age>25:
        print("These will be insuerd")
    else:
        print("These will be not insured")
else:
    print("The invalid data is enterd")
