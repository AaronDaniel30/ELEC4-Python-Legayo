# Name: Aaron Daniel A. Legayo
# Section: BSIT IV-C
# Activity: P4 - Safe Menu Program
# Date: November 21, 2026


def divide_numbers():
    print("\n===== DIVISION =====")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter numeric values.")

    except ZeroDivisionError:
        print("Error! You cannot divide by zero.")

    else:
        print(f"Result: {result}")

    finally:
        print("Division operation completed.")


def open_file():
    print("\n===== OPEN FILE =====")

    try:
        filename = input("Enter the file name: ")

        with open(filename, "r") as file:
            contents = file.read()

    except FileNotFoundError:
        print("Error! The file does not exist.")

    except PermissionError:
        print("Error! You do not have permission to open this file.")

    else:
        print("\nFile Contents:")
        print(contents)

    finally:
        print("File operation completed.")


def main():
    print("===================================")
    print("       SAFE MENU PROGRAM")
    print("Student: Aaron Daniel A. Legayo")
    print("Section: BSIT IV-C")
    print("===================================")

    while True:
        print("\n========== MENU ==========")
        print("1. Divide Numbers")
        print("2. Open a File")
        print("3. Exit")

        try:
            choice = input("Choose an option (1-3): ")

            if choice == "1":
                divide_numbers()

            elif choice == "2":
                open_file()

            elif choice == "3":
                print("Thank you for using the program!")
                break

            else:
                raise ValueError("Invalid menu selection.")

        except ValueError as error:
            print(f"Error: {error}")
            print("Please select only 1, 2, or 3.")


if __name__ == "__main__":
    main()