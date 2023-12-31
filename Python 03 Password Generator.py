#Task03
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Invalid length. Please enter a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    password = generate_password(length)

    print("\nGenerated Password:")
    print(password)

if __name__ == "__main__":
    main()
