# Encryption-Decryption Program
# Copyright (c) 2026 Arhaan Patolia

from cryptography.fernet import Fernet, InvalidToken
import time
import sys
# Files Used To Store Encrypted & Decrypted Data
output_enc = "output_encrypted.txt"
output_dec = "output_decrypted.txt"
# Function To Encrypt Data
def encrypt():
    message = input("Enter the data to encrypt: ")
    if not message:     # Prevent Empty Messages From Being Encrypted
        print("Error: Message cannot be empty.")
        return
    # Generate A Unique Key Which Will Be Used To Encrypt Or Decrypt The Data
    key = Fernet.generate_key()
    cipher = Fernet(key)

    print("Here Is The Key To Decrypt The Data: ", key.decode())
    # Encrypt The User's Message
    encry = cipher.encrypt(message.encode())
    print("Saving Encrypted Data Into A File...")
    time.sleep(1)
    # Save The Encrypted Data Into A File
    with open(output_enc, "ab") as file:
        file.write(b"\nOutput: \n")
        file.write(encry)
    print("\n----------------------------------------------------------------------")
    print("\nEnter Another Task To Do!\n")
# Function To Decrypt Data Using A Key
def decrypt():
    try:
        decrypt_key = input("Enter The Key To Decrypt Data: ").encode()
        # Create A Fernet Object Using The Provided Key
        fern = Fernet(decrypt_key)
        text = input("Enter The Message To Decrypt: ")
        # Decrypting The User's Data Using The Provided Key
        decrypted = fern.decrypt(text.encode())
        print(f"Decrypted Data: {decrypted.decode()}")
        time.sleep(1)   # Simulate Processing Time For Better User Experience
        print("Saving Decrypted Data Into A File...")
        time.sleep(1)
        # Save The Decrypted Data Into A File
        with open(output_dec, "ab") as file:
            file.write(b"\nOutput: \n")
            file.write(decrypted)
    except ValueError:       # Handle Invalid Or Malformed Keys
        print("Invalid Key Format!")
    except InvalidToken:    # Triggered When The Wrong Key Or Invalid Ciphertext Is Provided
        print("Decryption Failed!\nWrong Key Was Entered!")
    print("\n----------------------------------------------------------------------")
    print("\nEnter Another Task To Do!\n")

# Display Program Header And Instructions
print("----------------------------------------------------------------------")
print("| This Program Will Automate The Encryption And Decryption", " " * 9, "|\n| Of Data/Information Using A Key & Saves Data In A File", " " * 11, "|")
print("----------------------------------------------------------------------")
print("| BY: Arhaan Patolia |\n----------------------")
print("\nNOTE: PLEASE TAKE NOTE OF THE DECRYPTION KEY GIVEN DURING\n", " " * 4, "ENCRYPTION, ELSE YOU WON'T BE ABLE TO DECRYPT DATA!")

while True:
    # Display Program Menu
    print("\n1. Encrypt Data",
          "\n2. Decrypt Data",
          "\n3. Exit Program\n")

    choice = input("Enter Your Choice: ").strip()
    # Validate User Input
    while True:
        if choice == "1":
            encrypt()
            break
        elif choice == "2":
            decrypt()
            break
        elif choice == "3":
            sys.exit()
        else:
            print("\nInvalid Choice!\nChoose From 1, 2 or 3!")
            choice = input("Enter Your Choice: ").strip()
