#1ST
try:
    numerator=int(input())
    denominator=int(input())
    result = numerator // denominator
    print("Result:", result)
except ZeroDivisionError:
    print(" Division by zero is not allowed.")
#2nd
try:
    numerator = int(input())
    denominator = int(input())
    result = numerator // denominator
    print(result)
except ZeroDivisionError:
    print("Division by zero is not allowed")
finally:
    print("Division attempt complete.")

#3rd
T = int(input())
E = list(map(int, input().split()))
L = list(map(int, input().split()))

max_guests = 0
current_guests = 0

for i in range(T):
    current_guests += E[i] - L[i]
    if current_guests > max_guests:
        max_guests = current_guests

print(max_guests)
#4th
try:
    n=int(input())
    print(n*n)
except ValueError:
    print("Invalid input, please enter a number.")
#5th
class InvalidAgeException(Exception):
    def _init_(self, message="Age must be 18 or older"):
        super()._init_(message)

def validate_age(age):
    if age < 18:
        raise InvalidAgeException("Age must be 18 or older")
    print("Access granted")

try:
    age = int(input())
    validate_age(age)
except InvalidAgeException as e:
    print(f"InvalidAgeException: {e}")
except ValueError:
    print("Invalid input: Please enter a valid integer for age.")
#7th
# Custom Exception Class
class InvalidPinException(Exception):
    def _init_(self, message="Incorrect PIN entered"):
        super()._init_(message)

# Function to validate the PIN
def validate_pin(pin):
    if pin != 1234:
        raise InvalidPinException()
    print("Access granted")

# Main logic
try:
    pin = int(input())
    validate_pin(pin)
except InvalidPinException as e:
    print(f"InvalidPinException: {e}")
except ValueError:
    print("Invalid input: Please enter a valid integer for PIN.")
#8th
import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9_.%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}$"
    return re.match(pattern, email) is not None

# Read input from user
email = input()

# Check validity and print result
if is_valid_email(email):
    print("Invalid Email")
else:
    print("Valid Email")