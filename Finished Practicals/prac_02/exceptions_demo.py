"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
It occurs when a non-integer character has been inputted into either the denominator or the numerator

2. When will a ZeroDivisionError occur?
It occurs when the denominator equals to 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
No. A user inputting "0" in the denominator will always cause the ZeroDivisionError to occur.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
