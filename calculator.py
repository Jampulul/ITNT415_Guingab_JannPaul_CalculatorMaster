def addition():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 + num2
        print(f"Addition result: {result:g}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def subtraction():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 - num2
        print(f"Subtraction result: {result:g}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def multiplication():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 * num2
        print(f"Multiplication result: {result:g}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")


def division():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = num1 / num2
        print(f"Division result: {result:g}")
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")


def main():
    while True:
        print("\n================================")
        print("       CALCULATOR MASTER")
        print("       Jann Paul A. Guingab")
        print("================================")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            multiplication()
        elif choice == "4":
            division()
        elif choice == "5":
            print("Thank you for using Calculator Master!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 5.")


if __name__ == "__main__":
    main()
