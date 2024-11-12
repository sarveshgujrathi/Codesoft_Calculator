def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is undefined."
        else:
            return num1 / num2
    else:
        return "Invalid operation selected."

# Main function to run the calculator
def main():
    print("Welcome to the Simple Calculator!")

    # Input numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Invalid input. Please enter numeric values.")
        return

    # Input operation choice
    print("Select an operation:")
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    operation = input("Enter your choice of operation (+, -, *, /): ")

    # Perform the calculation
    result = calculate(num1, num2, operation)

    # Display the result
    print(f"Result: {result}")

# Run the calculator
if _name_ == "_main_":
    main()