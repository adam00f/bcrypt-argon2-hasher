DDDD   UUU   UUU  SSSSS   EEEEE   YY   YY
D   D  UUU   UUU S     S  E        YY YY 
D   D  UUU   UUU S         EEEEEE    YYY  
D   D  UUU   UUU  SSSSS    E         YYY  
D   D  UUU   UUU      S    E        YYY   
DDDD    UUUUUUU   SSSSS     EEEEE   YYY    

# bcrypt-argon2 password hasher


[![License](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://opensource.org/licenses/GPL-3.0)

This repository contains a collection of open-source scripts for password management tasks.

## Scripts Overview

- `main_menu.py`: Displays a main menu with options to execute different password management tasks.
- `pepperpepper.py`: Generates a pepper key for password hashing.
- `doubletrouble.py`: Performs double hashing of a password using bcrypt and Argon2 algorithms.
- `decrypt-script.py`: Decrypts an encrypted file using a provided key.
- `decrypt-script-test.py`: Tests the decryption functionality by encrypting and decrypting a sample file.
- `script.sh`: Bash script to update or install dependencies required for the scripts.

## Dependencies

- Python 3
- Git
- OpenSSL

## Usage

1. Clone the repository:
    git clone https://github.com/adam00f/bcrypt-argon2-hasher.git
    cd password-management-scripts

2. Make the scripts executable:
    chmod +x main_menu.py pepperpepper.py doubletrouble.py decrypt-script.py decrypt-script-test.py script.sh

3. Run the dependency installation script:
    sh script.sh or ./script.sh
    #This script will detect the Linux distribution and package manager, refresh package repositories, and install or update the required dependencies.

4. Run the main menu script:
    python3 main_menu.py
    #This will display a main menu with different options to choose from. Select the desired script by entering the corresponding option number.

5. Follow the prompts and provide any required input or passwords.

6. The scripts will perform the specified tasks and provide relevant output or save files in the appropriate locations.

Please make sure to read the script descriptions and usage instructions within the script files for more detailed information.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

These scripts are provided as-is without any warranty. Use them at your own risk.

