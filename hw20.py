#Name:ethan morris
#Class: 5th Hour
#Assignment: HW20
from hw19 import count

#1. Create a try catch that tries to print variable x (which has no value), but prints "Hello World!" instead.
try:
    print(x)
except NameError:
    print("Hello World!")


#2. Create a try catch that tries to divide 100 by whatever number the user inputs, but prints an exception for Divide By Zero errors.
try:
    user_input = int(input("type a number to divide 100: "))
    result = 100 / user_input
    print("Result:", result)
except ZeroDivisionError:
    print("Exception:cannot divide by zero.")

#3. Create a variable that asks the user for a number. If the user input is not an integer, prints an exception for Value errors.
try:
    user_input = int(input("enter an interger"))
    print(f"you entered:{user_input}")
except ValueError:
    print("exception: wrong input. please enter an integer.")

#4. Create a while loop that counts down from 5 to 0, but raises an exception when it counts below zero.
counter = 5
while counter >= 0:
    print(counter)
    counter -= 1
    if counter < 0:
        raise Exception("Error: Counter went below zero.")




