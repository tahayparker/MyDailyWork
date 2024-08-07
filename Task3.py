import random
import string

def password_generator(length):
    # Generate a password of the specified length
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password

def main():
    # Prompt the user to specify the desired length of the password
    length = int(input("Enter the desired length of the password: "))
    # Generate a password of the specified length
    password = password_generator(length)
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()