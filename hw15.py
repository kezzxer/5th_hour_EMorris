#Name: Ethan Morris
#Class: 5th Hour
#Assignment: HW15
import random
#1. Create a def function that prints out "Hello World!"
def hello_world():
    print("Hello World!")
hello_world()
#2. Create a def function that calculates the average of three numbers.
def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average
result = calculate_average(3807, 4206, 280)
print(f"The average is: {result}")
#3. Create a def function with the names of 5 animals as arguments, treats it like a list, and
#prints the name of the third animal.
def animal_list(*animal):
    print("The 3nd animal is", animal[2])

animal_list("zbra", "wolf", "racoon","monkey","kitty")
#4. Create a def function that loops from 1 to the number put in the argument.
def loop_to_number(n):
  for i in range(1, n + 1):
    print(i)

loop_to_number(5)
#5. Call all of the functions created in 1 - 4 with relevant arguments.
# 1. Call function that prints out "Hello World!"
hello_world()

# 2. Call function to calculate the average of three numbers
result = calculate_average(3807, 4206, 280)
print(f"The average is: {result}")

# 3. Call function with the names of 5 animals as arguments and print the 3rd one
animal_list("zebra", "wolf", "raccoon", "monkey", "kitty")

# 4. Call function to loop from 1 to the number put in the argument
loop_to_number(5)