calculator.py
# Continuous Basic Calculator Program

print("Welcome to the Python Calculator! 🐍")
print("You can perform +, -, *, / operations.")
print("Type 'exit' at any time to quit.\n")

while True:
    # Ask the user to input two numbers
    num1_input = input("Enter the first number (or 'exit' to quit): ")
    if num1_input.lower() == "exit":
        print("Goodbye! 👋")
        break
    num2_input = input("Enter the second number (or 'exit' to quit): ")
    if num2_input.lower() == "exit":
        print("Goodbye! 👋")
        break

    try:
        num1 = float(num1_input)
        num2 = float(num2_input)
    except ValueError:
        print("Invalid number! Please enter numeric values.\n")
        continue

    # Ask the user to choose an operation
    operation = input("Enter an operation (+, -, *, /): ")

    # Perform the operation
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation!"

    # Print the result
    print(f"{num1} {operation} {num2} = {result}\n")
