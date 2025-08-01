#1st code
def solve(n):
    full_crates = n // 12
    leftover_bottles = n % 12

    print("Full crates:", full_crates)
    print("Leftover bottles:", leftover_bottles)
n = int(input())
solve(n)
#2nd code
class Student:
    """
    A class to represent a student.
    """
    def _init_(self, student_id, student_name):
        """
        Initializes the Student object with an ID and name.
        """
        self.id = student_id
        self.name = student_name

    def display(self):
        """
        Prints the student's ID and name, each on a new line.
        """
        print(self.id)
        print(self.name)

# Main part of the program
if _name_ == "_main_":
    # Read the student ID from user input and convert it to an integer
    student_id_input = int(input())

    # Read the student name from user input
    student_name_input = input()

    # Create an instance of the Student class
    student = Student(student_id_input, student_name_input)

    # Call the display method to print the details
    student.display()
#3rd code
class Student:
    def _init_(self, student_id, student_name):
        self.id = student_id
        self.name = student_name

    def display(self):
        print(self.id)
        print(self.name)

if _name_ == "_main_":
    n = int(input())  # Number of students
    students = []

    for _ in range(n):
        student_id = int(input())       # ID input
        student_name = input()          # Name input
        student = Student(student_id, student_name)
        students.append(student)

    for student in students:
        student.display()
#4th code
class Calculator:
    MULTIPLIER = 1  

    def calculate_square(self, number):
        return number * number

number = int(input())
calc = Calculator()
print(calc.calculate_square(number))
#5th code
def compute_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())

print(compute_gcd(a, b))
#6th code
def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n
num = int(input())
print(digital_root(num))
#7th code
class Outer:
    def _init_(self, data):
        self.data = data

    class Inner:
        def _init_(self, outer_instance):
            self.outer_instance = outer_instance

        def display(self):
            print(f"Outer data: {self.outer_instance.data}")

# Main program
n = int(input())
values = list(map(int, input().split()))

for value in values:
    outer = Outer(value)
    inner = outer.Inner(outer)
    inner.display()
#8th code
n = int(input()) 

square = n * n
digit_sum = sum(int(digit) for digit in str(square))

if digit_sum == n:
    print("Yes")
else:
    print("No")