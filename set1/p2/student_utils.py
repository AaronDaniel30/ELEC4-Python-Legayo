# Name: Aaron Daniel A. Legayo
# Section: BSIT IV-C
# Activity: P2 - Custom Module
# Date: November 21, 2026

def calculate_average(grades):
    return sum(grades) / len(grades)


def determine_status(grades):
    if calculate_average(grades) >= 75:
        return "PASSED"
    return "FAILED"


def get_highest(grades):
    return max(grades)


def get_lowest(grades):
    return min(grades)