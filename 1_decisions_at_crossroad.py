# Task 1 Code Correction

number = float(input("Enter a number: "))
# adding conversion to float to help eliminate potential user errors/bugs

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
elif number < 0:
    print("The number is negative.")
else:
    print("A valid number was not entered. Please ensure input is formatted with Arabic numerals/digits.")
'''
I made three main changes after initially adding the float conversion to the input.
First I changed the first elif from a single = that is generally used for assignment
to a double == that is used for comparison. The second change I made was turning the original else statement
to a second elif as else cannot be followed by anything other than a colon.
Furthermore I did this because instead of making all other inputs negative I wanted to include the new else
statement I wrote which will notify the end user if they input an invalid string statement.
'''