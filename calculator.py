def addition():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print("Result:", num1 + num2)
    except ValueError:
        print("Invalid input. Please enter numbers.")


def main():
    print("================================")
    print("       CALCULATOR MASTER")
    print("       Jann Paul A. Guingab")
    print("================================")
    print("1. Addition")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        addition()
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
