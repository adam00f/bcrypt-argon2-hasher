import os
import time
from cryptography.fernet import Fernet
import getpass
import shutil
from termcolor import colored

# Prompt for the encryption password
encryption_password = getpass.getpass("Enter the password used for encryption: ")

# Load the encrypted password file and the encryption key
file_path = os.path.expanduser('~/.config/doublehashed_password.txt.enc')
key_file_path = os.path.expanduser('~/.config/doublehashed_key.txt')

# Load the encryption key
with open(key_file_path, 'rb') as key_file:
    key = key_file.read()

# Decrypt the password file
cipher_suite = Fernet(key)
with open(file_path, 'rb') as encrypted_file:
    encrypted_password = encrypted_file.read()

# Decrypt the password file using the encryption password
try:
    decrypted_password = cipher_suite.decrypt(encrypted_password).decode('utf-8')
except Exception:
    print(colored("Failed to decrypt the password file. Please check the encryption password.", 'red'))
    exit()

# Check if the entered password matches the encryption password
if decrypted_password != encryption_password:
    print(colored("Incorrect encryption password. Please try again.", 'red'))
    exit()

# Rest of the script...

# Prompt for the action
print("Select an action:")
print("1. Retrieve BCrypt Hashed Password")
print("2. Retrieve Argon2 Hashed Password")
print("3. Retrieve Double-Hashed Password")
print("4. Display all keys")
print("5. Secure Erase Keys and Hashes")
print("x. Quit")
choice = input("Enter your choice (1, 2, 3, 4, 5, or x): ")

# Check the choice and perform the corresponding action
if choice == '1':
    # Retrieve the BCrypt hashed password
    bcrypt_hashed_password = decrypted_password[:60]

    # Display the retrieved BCrypt hashed password
    print(colored("Retrieved BCrypt Hashed Password:", 'green'))
    print(bcrypt_hashed_password)

elif choice == '2':
    # Retrieve the Argon2 hashed password
    argon2_hashed_password = decrypted_password[60:]

    # Display the retrieved Argon2 hashed password
    print(colored("Retrieved Argon2 Hashed Password:", 'green'))
    print(argon2_hashed_password)

elif choice == '3':
    # Retrieve the double-hashed password
    double_hashed_password = decrypted_password[120:]

    # Display the retrieved double-hashed password
    print(colored("Retrieved Double-Hashed Password:", 'green'))
    print(double_hashed_password)

elif choice == '4':
    # Retrieve all the keys
    bcrypt_hashed_password = decrypted_password[:60]
    argon2_hashed_password = decrypted_password[60:]
    double_hashed_password = decrypted_password[120:]

    print(colored("All Keys:", 'green'))
    print("BCrypt Hashed Password:", bcrypt_hashed_password)
    print("Argon2 Hashed Password:", argon2_hashed_password)
    print("Double-Hashed Password:", double_hashed_password)

elif choice == '5':
    # Prompt for secure erase confirmation
    confirm = input(colored("This action will securely erase all keys and hashes. Enter 'DELETE' to proceed: ", 'yellow'))
    if confirm == 'DELETE':
        # Prompt for final acceptance before secure erase
        final_confirm = input(colored("This action is irreversible. Enter 'DELETE' to confirm: ", 'yellow'))
        if final_confirm == 'DELETE':
            # Secure erase the keys and hashes
            bcrypt_hashed_password = " " * 60
            argon2_hashed_password = " " * 60
            double_hashed_password = " " * 60

            # Write the securely erased keys and hashes back to the password file
            with open(file_path, 'w') as password_file:
                password_file.write(bcrypt_hashed_password + argon2_hashed_password + double_hashed_password)

            # Remove the encryption key file
            os.remove(key_file_path)

            print(colored("Keys and hashes securely erased.", 'green'))
        else:
            print(colored("Secure erase aborted.", 'yellow'))
    else:
        print(colored("Secure erase aborted.", 'yellow'))

elif choice == 'x':
    print(colored("Exiting the script.", 'green'))
    pass

else:
    print(colored("Invalid choice. Please select either 1, 2, 3, 4, 5, or x.", 'red'))
