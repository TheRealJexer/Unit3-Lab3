# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiply/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

def add(first_number, second_number):
    """This function ADDS two numbers inputed by the user"""
    return first_number + second_number

def subtract(first_number, second_number):
    """This funcint SUBTRACTS two numbers inputed by the user"""
    return first_number - second_number

def mulitply(first_number, second_number):
    """This function MULTIPLIES two numbers inputed by the user"""
    return first_number * second_number

def divide(first_number, second_number):
    """This function DIVIDES two numbers inputed by the user"""
    return first_number / second_number

if operation == "add":
    result = first_number + second_number
    print(f"Result: {result}")
elif operation == "subtract":
    result = first_number - second_number
    print(f"Result: {result}")
elif operation == "multiply":
    result = first_number * second_number
    print(f"Result: {result}")
elif operation == "divide":
    result = first_number / second_number
    print(f"Result: {result}")
else:
    print("Sorry, I do not understand your request.")