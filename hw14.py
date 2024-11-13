#Name:ethan morris
#Class: 5th Hour
#Assignment: HW14


#1. Create a variable that asks the user for an integer and an empty intger variable.
playerinput = int(input("select a number between one and ten"))

numb = 0
#2. Create a loop with a range from 1 to the number the user input.
for l in range (1, playerinput +1,):
    print(l)
    continue
#3. Use the loop to find the factorial of that number. A factorial of a number is that number multiplied
#by every number before it until you reach 1.
#For example: 5! is 5 x 4 x 3 x 2 x 1 = 120
def factorial(playerinput):
    if playerinput < 0:
        print("not defined for negative number")
        return
    elif playerinput == 0:
        return 1
    else:
        result = 1
        for w in range(1, playerinput +1):
            result *= w
        return result

#4. Print the factorial.
print(factorial(playerinput))