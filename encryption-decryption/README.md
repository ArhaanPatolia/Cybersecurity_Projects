# **Fernet Encryption/Decryption**

###### **Learning project - Not intended to protect real sensitive data.**



###### A small command-line program that encrypts and decrypts text using Fernet from Python's cryptography library.



### Features



* ###### Encrypt a typed message using a generated Fernet key
* ###### Decrypt a message by providing the key and the encrypted token
* ###### Saves encrypted output to output\_encrypted.txt and decrypted output to output\_decrypted.txt
* ###### Basic error handling for empty messages, malformed keys, and wrong keys or corrupted tokens



### Requirements



* ###### Python 3.8+
* ###### cryptography



###### bash

###### pip install cryptography



### Usage



###### bash

###### python encryption-decryption.py





#### You will see a menu:



###### 1\. Encrypt Data

###### 2\. Decrypt Data

###### 3\. Exit Program





### Encrypting



###### Choose 1 and enter your message.

###### The program generates a new key and prints it. Copy and store this key. It is not saved anywhere, and without it the data cannot be decrypted.

###### The encrypted token is appended to output\_encrypted.txt.



### Decrypting



###### Choose 2.

###### Enter the key that was shown during encryption.

###### Paste the encrypted token (copied from output\_encrypted.txt).

###### The decrypted message is printed and appended to output\_decrypted.txt.





### How It Works



###### Fernet.generate\_key() creates a random 32-byte key, URL-safe base64 encoded.

###### Fernet provides authenticated symmetric encryption (AES-128-CBC with HMAC-SHA256), so tampered or corrupted tokens fail to decrypt rather than returning garbage.

###### A new key is generated for every encryption, so each message has its own key.







### **Known Limitations**



###### This project is ***intentionally*** simple, and I'm aware of its weaknesses:

###### 

1. ###### The key is printed to the terminal and typed with input(), so it is visible in scrollback and while typing.
2. ###### Decrypted output is saved in plaintext to output\_decrypted.txt, which defeats the purpose of encrypting the data.
3. ###### No password-based key derivation. Users must copy and store a random key manually instead of using a password.
4. ###### Manual copy and paste. Tokens must be copied from the output file by hand; there is no "decrypt from file" option.
5. ###### Strings only. It does not encrypt or decrypt files.
6. ###### Output files accumulate. Entries are appended and never cleaned up.





### **Security Notice**



###### Do not use this program for passwords, personal records, or any data you cannot afford to lose or expose. Do not commit output\_encrypted.txt, output\_decrypted.txt, or any keys to version control.





## **Author**



##### Arhaan Patolia



