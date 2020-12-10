""" - Plain English

Create a list to store 5 Numbers (float)
capture the user's input 5 times for their grades
each time user input is captured, the number is appended to the list
the list will be sorted by ascending order, then spliced at index 2
once the highest number is aqquired we will sum them up and divde them by 3
a message will be outputted to the user
end

"""

""" - Pseudocode

create list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

capture input
append number to list

print a message to user

"""



grades = []

grade = input("Enter the 1st grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd grade: ")
grades.append(float(grade))

grade = input("Enter the 4th grade: ")
grades.append(float(grade))

grade = input("Enter the 5th grade: ")
grades.append(float(grade))

grades.sort()

grades = grades[2:]

grades = sum(grades)

outcome = grades / 3


print("Average Grade is:  {0:.2f}%".format(outcome))