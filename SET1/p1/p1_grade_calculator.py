# Name: Aaron Daniel A. Legayo
# Section: BSIT IV-C
# Activity: P1 - Student Grade Calculator
# Date: November 21, 2026

# Stores the student's grades
student_grades = []


# Function 1: Accept grades from the user
def enter_grades():
    grades = []

    while True:
        try:
            number_of_grades = int(input("How many grades will you enter? "))

            if number_of_grades > 0:
                break
            else:
                print("Please enter at least one grade.")

        except ValueError:
            print("Invalid input. Enter a whole number.")

    for i in range(number_of_grades):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Grade must be between 0 and 100.")

            except ValueError:
                print("Invalid input. Please enter a number.")

    return grades


# Function 2: Calculate the average
def calculate_average(grades):
    return sum(grades) / len(grades)


# Function 3: Get the highest grade
def get_highest(grades):
    return max(grades)


# Function 4: Get the lowest grade
def get_lowest(grades):
    return min(grades)


# Function 5: Determine pass or fail
def determine_status(grades):
    average = calculate_average(grades)

    if average >= 75:
        return "PASSED"
    else:
        return "FAILED"


# Function 6: Display the results
def display_results(grades):
    if not grades:
        print("\nNo grades available. Please enter grades first.")
        return

    print("\n========== STUDENT RESULTS ==========")
    print(f"Grades: {grades}")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest Grade: {get_highest(grades)}")
    print(f"Lowest Grade: {get_lowest(grades)}")
    print(f"Status: {determine_status(grades)}")
    print("=====================================")


# Main menu
def main():
    global student_grades

    print("\n Student: Legayo, Aaron Daniel A. | BSIT IV - C")

    while True:
        print("\n===== STUDENT GRADE CALCULATOR =====")
        print("1. Enter Grades")
        print("2. View Results")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            student_grades = enter_grades()
            print("\nGrades successfully saved!")

        elif choice == "2":
            display_results(student_grades)

        elif choice == "3":
            print("Thank you for using the Grade Calculator!")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()


# Local and Global Variables:
# A global variable can be accessed throughout the program.
# In this program, student_grades is a global variable because it is
# declared outside the functions. A local variable exists only inside
# the function where it is created. For example, grades inside
# enter_grades() is a local variable.