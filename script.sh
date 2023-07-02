#!/bin/bash

# Function to display status lines with color
status() {
	local message=$1
	local color=$2
	echo -e "\e[${color}m${message}\e[0m"
}

# Check Linux distribution and package manager
if [ -f /etc/os-release ]; then
	source /etc/os-release
	if [ "$(grep -Ei 'arch|endeavouros' <<<"$ID")" ]; then
		package_manager="pacman"
	elif [ "$ID" == "ubuntu" ] || [ "$ID" == "debian" ]; then
		package_manager="apt"
	elif [ "$ID" == "fedora" ]; then
		package_manager="dnf"
	elif [ "$ID" == "centos" ] || [ "$ID" == "rhel" ]; then
		package_manager="yum"
	else
		status "Unsupported Linux distribution" 91
		exit 1
	fi
else
	status "Unsupported Linux distribution" 91
	exit 1
fi

# Update and sync repositories
status "Refreshing package repositories..." 96
if [ "$package_manager" == "pacman" ]; then
	sudo pacman -Sy
elif [ "$package_manager" == "apt" ]; then
	sudo apt update
elif [ "$package_manager" == "dnf" ]; then
	sudo dnf update
elif [ "$package_manager" == "yum" ]; then
	sudo yum update
fi

# List of dependencies to check and install
dependencies=(
	python3
	git
	openssl
	python3-pip
	pip-click
	pip-getpass4
	pip-cryptography
	pip-fernet
	pip-termcolor
	pip-bcrypt
	pip-argon2
	pip-tqdm
	pip-pepper
	cargo
	gcc
)

# Install or update dependencies
status "Checking and installing dependencies..." 96
for dependency in "${dependencies[@]}"; do
	if ! command -v "$dependency" &>/dev/null; then
		status "Installing $dependency..." 93
		if [ "$package_manager" == "pacman" ]; then
			if [ "$dependency" == "python3" ]; then
				sudo pacman -S --noconfirm python
			else
				sudo pacman -S --noconfirm "$dependency"
			fi
		elif [ "$package_manager" == "apt" ]; then
			sudo apt install -y "$dependency"
		elif [ "$package_manager" == "dnf" ]; then
			sudo dnf install -y "$dependency"
		elif [ "$package_manager" == "yum" ]; then
			sudo yum install -y "$dependency"
		fi
	else
		status "$dependency is already installed" 92
	fi
done

# Install Python dependencies using pip
pip_dependencies=(
	click
	getpass4
	cryptography
	fernet
	termcolor
	bcrypt
	argon2
	tqdm
	pepper
)

status "Checking and installing Python dependencies..." 96
for pip_dependency in "${pip_dependencies[@]}"; do
	if ! python3 -m pip show "$pip_dependency" &>/dev/null; then
		status "Installing $pip_dependency..." 93
		python3 -m pip install "$pip_dependency"
	else
		status "$pip_dependency is already installed" 92
	fi
done

status "All dependencies have been installed or updated successfully!" 92
