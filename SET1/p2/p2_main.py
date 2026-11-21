# Name: Aaron Daniel A. Legayo
# Section: BSIT IV-C
# Activity: P2 - Custom Module
# Date: November 21, 2026

import student_utils
from datetime import datetime


def main():
    print("===================================")
    print("     STUDENT GRADE REPORT")
    print("===================================")
    print("Student: Aaron Daniel A. Legayo")
    print("Section: BSIT IV-C")
    print(f"Report Date: {datetime.now().strftime('%B %d, %Y %I:%M %p')}")

    grades = []

    while True:
        try:
            number = int(input("\nHow many grades will you enter? "))
            if number > 0:
                break
            print("Please enter at least one grade.")
        except ValueError:
            print("Invalid input. Enter a whole number.")

    for i in range(number):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a number.")

    print("\n========== RESULTS ==========")
    print(f"Grades: {grades}")
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print(f"Highest Grade: {student_utils.get_highest(grades)}")
    print(f"Lowest Grade: {student_utils.get_lowest(grades)}")
    print(f"Status: {student_utils.determine_status(grades)}")
    print("=============================")


if __name__ == "__main__":
    main()