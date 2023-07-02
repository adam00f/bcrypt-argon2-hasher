import click
import os


@click.group()
def cli():
    pass


@cli.command()
def guided_password_gen():
    # Run pepperpepper.py
    os.system("python3 pepperpepper.py")

    # Check if the pepper generation was successful
    pepper_file_path = os.path.expanduser('~/.config/pepper.txt')
    if not os.path.exists(pepper_file_path):
        click.echo("Failed to generate pepper key. Please try again.")
        return

    # Run doubletrouble.py
    os.system("python3 doubletrouble.py")


@cli.command()
def run_doubletrouble():
    # Run doubletrouble.py
    os.system("python3 doubletrouble.py")


@cli.command()
def run_decrypt_script():
    # Run decrypt-script.py
    os.system("python3 decrypt-script.py")


@cli.command()
def run_decrypt_script_test():
    # Run decrypt-script-test.py
    os.system("python3 decrypt-script-test.py")


@cli.command()
def check_updates():
    choice = input("Would you like to check for updates? (yes/no): ")
    if choice.lower() == "yes":
        os.system("bash script.sh")
        click.echo("Updates checked successfully.")
    else:
        click.echo("Skipping update check.")

    # Continue with the rest of the script
    # ...


if __name__ == "__main__":
    cli()
