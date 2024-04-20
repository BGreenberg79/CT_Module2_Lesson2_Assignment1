# Task 1 Leap Year Checker

year_to_check = int(input("Please enter a year: "))

if year_to_check % 4 == 0 and not year_to_check % 100 == 0:
    print("The year entered is a leap year.")
elif year_to_check % 400 == 0:
    print("The year entered is a leap year.")
else:
    print("The year entered is not leap year.")

'''
The first part of the program checks for a leap year by checking to see if the year
being divisble by 4 evaluates to true and if being divisible by 100 evaluates to false.
If both conditions are met it is a leap year. The elif checks for the divisble by 400 exception
and if it evaluates to true will return a leap year. 
The else statement returns all other years input as not a leap year.
'''