#Name: ethan morris
#Class: 5th Hour
#Assignment: HW19

#1. Import all the functions from the HW15 file.
from hw15 import hello_world, calculate_average
from hw15 import animal_list
from hw15 import loop_to_number
#2. Call the functions here and run HW19.
hello_world()
animal_list("zbra", "wolf", "racoon","monkey","kitty")
loop_to_number(5)


#3. Delete all calls from HW15 and run HW19 agai
try:
    user_input = int(input("Enter a number to divide 100: "))
    result = 100 / user_input
    print("Result:", result)
except ZeroDivisionError:
    print("Exception: Divide By Zero Error")
except ValueError:
    print("Exception: Invalid input. Please enter a valid number.")
try:
    user_input = int(input("Enter a number: "))
except ValueError:
    print("Exception: Invalid input. Not a valid integer.")
try:
    count = 5
    while count >= 0:
        print(count)
        count -= 1
    if count < 0:
        raise Exception("Count cannot go below zero!")
except Exception as e:
    print("Exception:", e)
