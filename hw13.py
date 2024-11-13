#Name: ethan morris
#Class: 5th Hour
#Assignment: HW13


#1. Create a list containing 10 integers of your choice.

l= [1,2,3,4,5,6,7,8,9,10]
#2. Create two empty variables named evenNumbers and oddNumbers.
evennumbers =0
oddNumbers = 0
#3. Make a loop that counts the number of even and odd numbers in the list.
#(HINT: The way to see if a number is even is if it is divisible by 2).
l = [1,2,3,4,5,6,7,8,9,10]

evennumbers, oddNumbers = 0, 0

# iterating each number in list
for num in l:

    # checking condition
    if num % 2 == 0:
        evennumbers += 1

    else:
        oddNumbers += 1
# Print the total count of even and odd numbers.
print("evenNumbers in the list: ", evennumbers)
print("oddNumbers in the list: ", oddNumbers)