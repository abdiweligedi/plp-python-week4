age = int(input("Enter your age: "))

if age < 18:
    consent = input("Do you have parental consent? (yes/no): ").lower()

    # A person under 18 must be at least 13 and have parental consent.
    if age >= 13 and consent == "yes":
        print("Welcome to the club!")
    else:
        print("Sorry, you are not eligible yet.")

else:
    # A person who is 18 or older does not need parental consent.
    if not age < 18:
        print("Welcome to the club!")
    else:
        print("Sorry, you are not eligible yet.")