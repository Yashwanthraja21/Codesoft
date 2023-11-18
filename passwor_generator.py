import secrets
import string

def generate_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator App!")
    while True:
        try:
            length = int(input("Enter the desired length of the password (at least 6 characters): "))
            if length < 6:
                print("Please enter a length of at least 6 characters.")
                continue
            password = generate_password(length)
            print("Generated Password:", password)
            break  # Exit the loop after generating the password
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()

