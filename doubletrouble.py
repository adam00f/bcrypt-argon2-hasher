import bcrypt
import argon2
import time
import os
import getpass
import binascii
from termcolor import colored
from tqdm import tqdm
from cryptography.fernet import Fernet

# Prompt for password to use for hashing
password = getpass.getpass("Enter the password to hash: ")

# Define the file path of the pepper secret key
pepper_file_path = os.path.expanduser('~/.config/pepper.txt')

# Read the pepper secret key from the file
with open(pepper_file_path, 'r') as pepper_file:
    pepper = pepper_file.read().strip()

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()
        encrypted_data = Fernet(key).encrypt(data)
    with open(file_path + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)

# First round of hashing with bcrypt
print(colored("Performing first round of hashing with bcrypt...", 'yellow'))
cost_bcrypt = 15  # Adjust the cost factor (higher is more secure but slower)
salt_bcrypt = bcrypt.gensalt(rounds=cost_bcrypt)
hashed_password_bcrypt = bcrypt.hashpw((password + pepper).encode('utf-8'), salt_bcrypt)
print(colored("First round of hashing with bcrypt completed.", 'green'))
print()

# Second round of hashing with Argon2
print(colored("Performing second round of hashing with Argon2...", 'yellow'))
time_cost_argon2 = 3  # Adjust the time cost (higher is more secure but slower)
# Adjust the memory cost (higher is more secure but requires more memory)
memory_cost_argon2 = 131072
# Adjust the parallelism factor (higher is more secure but requires more CPU cores)
parallelism_argon2 = 3
hash_len_argon2 = 32  # Adjust the desired output hash length (in bytes)
salt_argon2 = b'somesalt'
argon2_params = {
    'time_cost': time_cost_argon2,
    'memory_cost': memory_cost_argon2,
    'parallelism': parallelism_argon2,
    'hash_len': hash_len_argon2,
    'type': argon2.Type.ID
}
argon2_hasher = argon2.PasswordHasher(**argon2_params)

# Use tqdm for progress bar
print("Progress for the second round of hashing:")
progress_bar = tqdm(total=100, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}')

# Simulate progress for the second round of hashing
for i in range(100):
    # Simulating work being done
    time.sleep(0.05)
    progress_bar.update(1)

hashed_password_double = argon2_hasher.hash(
    (hashed_password_bcrypt.decode('utf-8') + salt_argon2.decode('utf-8') + pepper).encode('utf-8'))
progress_bar.close()

print(colored("\nSecond round of hashing with Argon2 completed.", 'green'))
print()

# Save the double-hashed password to a secure file
file_path = os.path.expanduser('~/.config/doublehashed_password.txt')
password_file = open(file_path, 'w')
password_file.write(hashed_password_double)
password_file.close()

print("Double-hashed password saved to:", colored(file_path, 'cyan'))

# Display the final hash
print(colored("Final Hash:", 'cyan'))
print(hashed_password_double)

# Prompt for password to use for encryption
encryption_password = getpass.getpass("Enter password for encryption: ")

# Encrypt the password file
key = Fernet.generate_key()
cipher_suite = Fernet(key)
encrypted_password = cipher_suite.encrypt(hashed_password_double.encode('utf-8'))

with open(file_path + '.enc', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_password)

# Save the encryption key to a file
key_file_path = os.path.expanduser('~/.config/doublehashed_key.txt')
with open(key_file_path, 'wb') as key_file:
    key_file.write(key)

print("Encrypted password file saved to:", file_path + '.enc')
print("Encryption key saved to:", key_file_path)
