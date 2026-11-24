
# Name: Aaron Daniel Legayo
# Section: IV-BSIT
# Activity: P6 - Recursion Toolkit
# Date: November 24, 2026

# Base case: If n is 0 or 1, return 1.
# Recursive call: Multiply n by factorial of n - 1.
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Base case: If n is 0 or 1, return n.
# Recursive call: Add the two previous Fibonacci numbers.
def fibonacci(n):
    if n < 0:
        raise ValueError("Please enter a non-negative number.")
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: If n is 0, return 0.
# Recursive call: Add n to the sum of numbers from 1 to n - 1.
def sum_numbers(n):
    if n < 0:
        raise ValueError("Please enter a non-negative number.")
    if n == 0:
        return 0
    return n + sum_numbers(n - 1)


# Base case: If the list is empty, the target was not found.
# Recursive call: Search the remaining list one item at a time.
def search(items, target):
    if not items:
        return False
    if items[0] == target:
        return True
    return search(items[1:], target)


def main():
    while True:
        print("\n================================")
        print("       RECURSION TOOLKIT")
        print("================================")
        print("Prepared by: Aaron Daniel Legayo")
        print("1. Factorial")
        print("2. Fibonacci")
        print("3. Sum of Numbers")
        print("4. Search an Item")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        try:
            if choice == "1":
                number = int(input("Enter a non-negative number: "))
                print("Factorial:", factorial(number))

            elif choice == "2":
                number = int(input("Enter the number of Fibonacci terms: "))
                if number < 0:
                    raise ValueError("Please enter a non-negative number.")

                # Display the first n Fibonacci terms.
                terms = [fibonacci(i) for i in range(number)]
                print("Fibonacci sequence:", terms)

            elif choice == "3":
                number = int(input("Enter a non-negative number: "))
                print("Sum:", sum_numbers(number))

            elif choice == "4":
                values = input("Enter numbers separated by spaces: ")
                items = [int(value) for value in values.split()]
                target = int(input("Enter the number to search for: "))

                if search(items, target):
                    print(target, "was found in the list.")
                else:
                    print(target, "was not found in the list.")

            elif choice == "5":
                print("Thank you for using the Recursion Toolkit!")
                break

            else:
                print("Invalid choice. Please select 1 to 5.")

        except ValueError as error:
            print("Invalid input:", error)


if __name__ == "__main__":
    main()
