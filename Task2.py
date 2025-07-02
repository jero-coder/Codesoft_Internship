import random
import string

def generate_password(length):
    if length < 4:
        return "Password length must be at least 4 characters."

    # Characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")
    print("---------------------")

    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

# Run the program
main()
