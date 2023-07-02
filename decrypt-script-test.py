import os
import time
from cryptography.fernet import Fernet
import getpass
import shutil
from termcolor import colored

# Prompt for the encryption password
encryption_password = getpass.getpass("Enter the password used for encryption: ")

# Generate the encryption key
key = Fernet.generate_key()

# Write the encryption key to a file
key_file_path = os.path.expanduser('~/.config/pepper-test-key.txt')
with open(key_file_path, 'wb') as key_file:
    key_file.write(key)

# Encrypt the test file
file_path = os.path.expanduser('~/.config/pepper-test.txt')
cipher_suite = Fernet(key)
encrypted_data = cipher_suite.encrypt(encryption_password.encode('utf-8'))

# Write the encrypted test data to the file
with open(file_path, 'wb') as encrypted_file:
    encrypted_file.write(encrypted_data)

print("Encrypted test file saved to:", file_path)
print("Encryption key saved to:", key_file_path)

# Load the encrypted test file and the encryption key
with open(key_file_path, 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)
with open(file_path, 'rb') as encrypted_file:
    encrypted_data = encrypted_file.read()

# Decrypt the test file using the encryption password
try:
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode('utf-8')
except Exception:
    print(colored("Failed to decrypt the test file. Please check the encryption password.", 'red'))
    exit()

# Check if the entered password matches the encryption password
if decrypted_data != encryption_password:
    print(colored("Incorrect encryption password. Please try again.", 'red'))
    exit()

# Rest of the script...

# Prompt for the action
print("Select an action:")
print("1. Retrieve Test Key")
print("2. Secure Erase Test Key")
print("x. Quit")
choice = input("Enter your choice (1, 2, or x): ")

# Check the choice and perform the corresponding action
if choice == '1':
    # Retrieve the test key
    test_key = decrypted_data.strip()

    # Display the retrieved test key
    print(colored("Retrieved Test Key:", 'green'))
    print(test_key)

elif choice == '2':
    # Prompt for secure erase confirmation
    confirm = input(colored("This action will securely erase the test key. Enter 'DELETE' to proceed: ", 'yellow'))
    if confirm == 'DELETE':
        # Prompt for final acceptance before secure erase
        final_confirm = input(colored("This action is irreversible. Enter 'DELETE' to confirm: ", 'yellow'))
        if final_confirm == 'DELETE':
            # Secure erase the test key
            test_key = " " * len(decrypted_data)

            # Write the securely erased test key back to the file
            with open(file_path, 'wb') as test_key_file:
                test_key_file.write(cipher_suite.encrypt(test_key.encode('utf-8')))

            # Remove the encryption key file
            os.remove(key_file_path)

            print(colored("Test key securely erased.", 'green'))
        else:
            print(colored("Secure erase aborted.", 'yellow'))
    else:
        print(colored("Secure erase aborted.", 'yellow'))

elif choice == 'x':
    print(colored("Exiting the script.", 'green'))
    pass

else:
    print(colored("Invalid choice. Please select either 1, 2, or x.", 'red'))
