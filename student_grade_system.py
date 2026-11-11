"""Student Grade Management System (console version).

Accepts student marks, validates input, calculates the average mark and
letter grade for each student, and displays the results with a class summary.
"""

MIN_MARK = 0
MAX_MARK = 100
MIN_SUBJECTS = 1
MAX_SUBJECTS = 10
GRADE_SCALE = [(90, "A"), (80, "B"), (70, "C"), (60, "D"), (0, "F")]


def read_name(prompt="Student name: "):
    """F01 - ask for a non-empty student name."""
    while True:
        name = input(prompt).strip()
        if name:
            return name
        print("Error: the name cannot be empty.")


def read_int(prompt, low, high):
    """F02 - ask for a whole number between low and high."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
        except ValueError:
            print("Error: please enter a whole number.")
            continue
        if low <= value <= high:
            return value
        print(f"Error: enter a number from {low} to {high}.")


def read_mark(prompt):
    """F03 - ask for one mark and validate that it is 0-100."""
    while True:
        text = input(prompt).strip()
        try:
            mark = float(text)
        except ValueError:
            print("Error: the mark must be a number.")
            continue
        if MIN_MARK <= mark <= MAX_MARK:
            return mark
        print(f"Error: the mark must be between {MIN_MARK} and {MAX_MARK}.")


def calculate_average(marks):
    """F04 - average of a list of marks."""
    return sum(marks) / len(marks)


def assign_grade(average):
    """F05 - letter grade for an average mark."""
    for minimum, letter in GRADE_SCALE:
        if average >= minimum:
            return letter
    return "F"


def add_student():
    """F06 - collect one student's data and return a result record."""
    name = read_name()
    count = read_int(f"Number of subjects ({MIN_SUBJECTS}-{MAX_SUBJECTS}): ",
                     MIN_SUBJECTS, MAX_SUBJECTS)
    marks = [read_mark(f"  Mark for subject {i} ({MIN_MARK}-{MAX_MARK}): ")
             for i in range(1, count + 1)]
    average = calculate_average(marks)
    return {"name": name, "marks": marks,
            "average": average, "grade": assign_grade(average)}


def display_results(students):
    """F07 - print the results table."""
    print("\n" + "=" * 64)
    print(f"{'Name':<20}{'Marks':<24}{'Average':>9}{'Grade':>8}")
    print("-" * 64)
    for s in students:
        marks = ", ".join(f"{m:g}" for m in s["marks"])
        print(f"{s['name']:<20}{marks:<24}{s['average']:>9.2f}{s['grade']:>8}")
    print("=" * 64)


def class_summary(students):
    """F08 - print count, class average, highest and lowest average."""
    averages = [s["average"] for s in students]
    print(f"Students       : {len(students)}")
    print(f"Class average  : {calculate_average(averages):.2f}")
    print(f"Highest average: {max(averages):.2f}")
    print(f"Lowest average : {min(averages):.2f}")


def main():
    """F09 - add students until the user stops, then show the results."""
    print("STUDENT GRADE MANAGEMENT SYSTEM")
    students = []
    while True:
        students.append(add_student())
        again = input("Add another student? (y/n): ").strip().lower()
        if again != "y":
            break
    display_results(students)
    class_summary(students)


if __name__ == "__main__":
    main()
