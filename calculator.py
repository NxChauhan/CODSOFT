def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Main calculator program
while True:

    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        continue

    # Prompt the user to choose an operation
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    choice = input("Enter the number of the desired operation: ")


    # Perform the calculation and display the result
    if choice == '1':
        result = add(a, b)
        print(f"Result: {a} + {b} = {result}")
    elif choice == '2':
        result = subtract(a, b)
        print(f"Result: {a} - {b} = {result}")
    elif choice == '3':
        result = multiply(a, b)
        print(f"Result: {a} * {b} = {result}")
    elif choice == '4':
        result = divide(a, b)
        print(f"Result: {a} / {b} = {result}")
    elif choice == '5':
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid input. Please enter a valid operation choice.")
