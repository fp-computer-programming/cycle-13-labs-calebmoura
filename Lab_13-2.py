# Author: Caleb A. Moura

# Dictionary named grades which holds assignment names & grades.
grades = {
    "Engineering Quiz": 87,
    "Math Unit Test": 94,
    "Cartology Mini Quiz": 75,
    "Pre-Med Quiz": 68,
    "Bo-Engineering mini Quiz": 43
}

# List of all grades received printed using a one-line statement.
print(list(grades.values()))

# Name of each assignment in dictionary printed on a separate line by using a for loop.
for assignment in grades:
    print(assignment)

# Name and grade received on each assignment that scored a 70 or above printed using another for loop.
print("Grades 70 or above:")
for assignment, grade in grades.items():
    if grade >= 70:
        print(f"{assignment}: {grade}")

# Name and grade received on each assignment that scored a 50 or below on printed using another for loop.
print("Grades 50 or below:")
for assignment, grade in grades.items():
    if grade <= 50:
        print(f"{assignment}: {grade}")