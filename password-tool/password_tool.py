# Simple Password Generator/Strength Checker
# Copyright (c) 2026 Arhaan Patolia


# Import Required Libraries
import secrets
import string
import time
import sys
# Store Character Sets Used For Password Generation
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
punctuation = "!@#$%&*()_+-=<?>/~"

# Function Used To Generate A Random Password
def generate_password():
    print("\nPassword Generator!\n")
    while True:
        try:
            length = int(input("Enter The Length Of Password (At least 8 Characters): "))
            if length >= 8:
                break
            print("Length Must Be At Least 8!")       # Setting The Minimum Length To 8 Characters
        except ValueError:
            print("Please Enter A Valid Length!")

    password = ""
    print("\nGenerating Password...\n")
    time.sleep(1)           # Simulate Processing Time For Better User Experience
    for _ in range(length):
        # Randomly Choose A Character From All The Character Sets
        password += secrets.choice(lower + upper + digits + punctuation)
    print("\nGenerated Password: {}".format(password))
    print("\n------------------------------------------------------------")

# Function Used To Check The Strength Of A Password
def password_strength():
    print("\nPassword Strength Checker!\nThere Are 5 Password Strength Levels\n")
    password = input("Enter your password: ").strip()
    score = 0                  # The Score Will Be Used To Determine The Strength Of The Password
    # Prevent Empty Passwords From Being Checked
    while password == "":
        print("Please Enter A Password!")
        password = input("Enter your password: ").strip()

    print("\nChecking Password Strength...\n")
    time.sleep(1)

    # Length Checks
    if len(password) <= 6:      # Penalize Very Short Passwords
        score -= 1
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Character Type Checks
    # Award Points For Each Security Requirement Met
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    # Identify & Output The Level Strength (5 Levels)
    if score <= 1:
        print("Strength: Level 1/5 - Very Weak")
    elif score == 2:
        print("Strength: Level 2/5 - Weak")
    elif score == 3:
        print("Strength: Level 3/5 - Moderate")
    elif score == 4:
        print("Strength: Level 4/5 - Strong")
    elif score >= 5:
        print("Strength: Level 5/5 - Very Strong")
    # Footer
    print("\n------------------------------------------------------------")


print("------------------------------------------------------------")
print( "|", " " * 6, "Simple Password Generator/Strength Checker", " " * 6, "|")
print("------------------------------------------------------------")
print("BY: Arhaan Patolia |\n--------------------")

while True:
    # The Menu
    print("\n1. Generate Password"
          "\n2. Check Password Strength"
          "\n3. Exit\n")

    choice = input("Enter Your Choice: ").strip()
    while True:                              # Validates The User Input
        if choice == "1":
            generate_password()
            break
        elif choice == "2":
            password_strength()
            break
        elif choice == "3":
            print("\n------------------------------------------------------------\n")
            print("Exiting...")
            time.sleep(1)
            sys.exit()
        else:
            print("Please Enter A Valid Choice!")
            choice = input("Enter your choice: ").strip()