#SECTION D: Advanced / Thinking 
#16. Write a program: - Simulate login system - Use file to store username/password  
def login_system():
    username = input("Enter username: ")
    password = input("Enter password: ")

    try:
        with open("users.txt", "r") as file:
            for line in file:
                stored_user, stored_pass = line.strip().split(":")
                if username == stored_user and password == stored_pass:
                    print("Login successful!")
                    return
        print("Invalid username or password.")
    except FileNotFoundError:
        print("Error: User database not found.")

# To test, ensure a 'users.txt' exists with content like: admin:1234
login_system()

#17. Exception Handling: - Create custom exception "InvalidAgeError" - Raise error if age < 18 
class InvalidAgeError(Exception):
    """Raised when the input age is less than 18."""
    pass

def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 18:
            raise InvalidAgeError("Access denied. You must be at least 18 years old.")
        print("Age verified. Welcome!")
    except InvalidAgeError as e:
        print(f"Custom Error: {e}")
    except ValueError:
        print("Please enter a valid numerical age.")

check_age()   
