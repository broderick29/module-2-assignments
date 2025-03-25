# Author: Broderick Clapper
# File Name: module 2 lab BC
# assignment: deans list
# Description: This app accepts student names and GPAs, then checks if they qualify for the Dean's List or the Honor Roll.

while True:
    last_name = input("Enter student's last name (or 'ZZZ' to quit): ").strip()
    
    if last_name.upper() == 'ZZZ':
        print("Exiting program.")
        break

    first_name = input("Enter student's first name: ").strip()

    try:
        gpa = float(input("Enter student's GPA: "))
    except ValueError:
        print("Invalid input. Please enter a valid GPA.")
        continue

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print
