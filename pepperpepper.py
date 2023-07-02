import os
import binascii
import getpass
from cryptography.fernet import Fernet

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
        encrypted_data = Fernet(key).encrypt(data)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

pepper = os.urandom(32)  # Generate a random pepper

# Convert the pepper to hexadecimal representation
pepper_hex = binascii.hexlify(pepper).decode('utf-8')

print("Generated pepper (hex):", pepper_hex)

# Save the pepper to a secure file
file_path = os.path.expanduser('~/.config/pepper.txt')
pepper_file = open(file_path, 'w')
pepper_file.write(pepper_hex)
pepper_file.close()

print("Pepper saved to:", file_path)

# Prompt for password to use for encryption
encryption_password = getpass.getpass("Enter password for encryption: ")

# Encrypt the pepper file
key = Fernet.generate_key()
cipher_suite = Fernet(key)
encrypted_pepper = cipher_suite.encrypt(pepper)

with open(file_path + '.enc', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_pepper)

# Save the encryption key to a file
key_file_path = os.path.expanduser('~/.config/pepper_key.txt')
with open(key_file_path, 'wb') as key_file:
    key_file.write(key)

print("Encrypted pepper file saved to:", file_path + '.enc')
print("Encryption key saved to:", key_file_path)

