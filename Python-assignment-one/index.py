def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "You cannot divide a number by zero!"
    return x / y

def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Check your operation! You can only use +, -, *, /")
            return

        print(f"When Faith does this operation she gets {num1} {operation} {num2} is: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    main()