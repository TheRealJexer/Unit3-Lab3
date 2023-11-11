# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiply/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

def addition(operation):
    if operation == "add":
        output = first_number + second_number
        return output
    
def subtraction(operation):
    if operation == "subtract":
        output = first_number - second_number
        return output
    
def multiplication(operation):
    if operation == "multiply":
        output = first_number * second_number
        return output
    
def division(operation):
    if operation == "divide":
        output = first_number / second_number
        return output
    
def falseInput(operation):
    while operation != operation:
        print("Sorry, I do no understand your request.")
        break


print(f"Result: {output}")


# if operation == "add":
#     result = first_number + second_number
#     print(f"Result: {result}")
# elif operation == "subtract":
#     result = first_number - second_number
#     print(f"Result: {result}")
# elif operation == "multiply":
#     result = first_number * second_number
#     print(f"Result: {result}")
# elif operation == "divide":
#     result = first_number / second_number
#     print(f"Result: {result}")
# else:
#     print("Sorry, I do not understand your request.")