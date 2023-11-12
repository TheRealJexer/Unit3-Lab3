import calculator

# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

inputList = ["add", "subtract", "multiply", "divide"]

if operation == "add":
    result = calculator.add(first_number, second_number)
    print(f"Result is: {result}")
elif operation == "subtract":
    result = calculator.subtract(first_number, second_number)
    print(f"Result is: {result}")
elif operation == "multiply":
    result = calculator.mulitply(first_number, second_number)
    print(f"Result is {result}")
elif operation == "divide":
    result = calculator.divide(first_number, second_number)
    print(f"Result is: {result}")
else:
    print("sorry, I do not understand your request")
        


