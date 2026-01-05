# variable naming
import math
student_count = 1000
print(student_count)
rating = 4.99
is_published = True
course_name = "python programing"

# strings
course = "Python Programming"
# function - a resuble peice of code that can be used later.
print(len(course))  # len is used to get length of the string
print((course[0]))  # retuns the first letter
print((course[-1]))  # retuns the last letter
print((course[0:3]))  # returns the firts three letters
print((course[0:]))  # return the whole string
print((course[:3]))  # returns the firts three letters
print((course[:]))  # return the whole string

# Escape sequences
course = "Python \"Programming"
# backslash is an escape caracter while backslash and " is a secuence
# \"
# \'
# \\
# \n

# Formmated string
first = "Yurub"
last = "Hillow"
full = first + " " + last
full = f"{len(first)} {last}"
print(full)

# string methods
course = "    Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.replace("P", "J"))
print("Pro" in course)
print("swift" not in course)

# Numbers
x = 1
x = 1.1
x = 1 + 2j  # a + bi
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)

# working with a number
print(round(2.9))
print(abs(2.9))

print(math.ceil(2.2))

# type conversation
a = input("a: ")
b = int(a) + 15
print(f"a: {a}, b: {b}")

# falsy value in python:
# ""
# 0
# none
print(bool("false"))
