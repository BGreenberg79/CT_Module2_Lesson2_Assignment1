# Task 1 Ideentify the Greatest

number_a = float(input("Please enter your first number: "))
number_b = float(input("Please enter your second number: "))
number_c = float(input("Please enter your third number: "))

if number_a > number_b and number_a > number_c:
    print("Your first number is the largest.")
elif number_b > number_a and number_b  > number_c:
    print("Your second number is the largest.")
elif number_c > number_a and number_c > number_b:
    print("Your third number is the largest.")
else:
    print("Please ensure that all three entries are valid numerals.")
# This program uses an and statement to ensure that the largest number is identified without having a messier expression that accounts for every permutation (i.e. a > b > c, a > c > b, etc.)

# Task 2: Identify the smallest
if number_a < number_b and number_a < number_c:
    print("Your first number is the smallest.")
elif number_b < number_a and number_b < number_c:
    print("Your second number is the smallest.")
elif number_c < number_a and number_c < number_b:
    print("Your third number is the smallest.")
else:
    print("Please ensure all three inputs are valid numerals.")
# This extension uses the same logic and mechanics from the first task but flips the operators to identify the minimum instead of the maximum.

# Task 3: Equality Check
if number_a == number_b == number_c:
    print(f"Your three numbers are all {number_a}, and thus are equal.")
elif number_a == number_b and number_a > number_c:
    print(f"Your first two numbers are both {number_a} and are larger than the smallest number, {number_c}.")
elif number_a == number_c and number_a > number_b:
    print(f"Your first and last numbers are both {number_a} and are larger than the smallest number, {number_b}.")
elif number_b == number_c and number_b > number_a:
    print(f"Your second and last numbers are both {number_b} and are larger than the smallest number {number_a}.")
elif number_a > number_b > number_c:
    print(f"Your first number, {number_a}, is largest. Your last number, {number_c}, is smallest.")
elif number_a > number_c > number_b:
    print(f"Your first number, {number_a}, is largest. Your second number, {number_b}, is smallest.")
elif number_b > number_c > number_a:
    print(f"Your second number, {number_b}, is largest. Your first number, {number_a}, is smallest.")
elif number_b > number_a > number_c:
    print(f"Your second number, {number_b}, is largest. Your last number, {number_c}, is smallest.")
elif number_c > number_b > number_a:
    print(f"Your last number, {number_c}, is largest. Your first number, {number_a} is smallest.")
elif number_c > number_a > number_b:
    print(f"Your last number, {number_c}, is largest. Your second number, {number_b}, is smallest.")
else:
    print("Please check to make sure all three inputs are numerals.")

'''
This version of the program accounts for every single permutation including the user potentially entering values that may be equal to each other.
This version also uses f-strings to identify the number's input in the print statement that is returned.
'''