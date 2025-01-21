#Name:
#Class: 5th Hour
#Assignment: HW17


#1. Import the "random" library and create a def function that prints "Hello World!"
import random

def hello_world():
    print("Hello World!")
#2. Create two empty integer variables named "heads" and "tails"
heads = 0
tails = 0
#3. Create a def function that flips a coin one hundred times and increments the result in the above variables.
def flip_coin():
    global heads,tails
    for _ in range(100):
        flip = random.choice(["heads","tails"])
        if flip =="heads":
            heads += 1
        else:
            tails += 1
#4. Call the "Hello world" and "Coin Flip" functions here
hello_world()
flip_coin()
#5. Print the final result of heads and tails here
print("heads:",heads)
print("tails",tails)