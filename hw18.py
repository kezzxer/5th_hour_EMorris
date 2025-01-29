#Name:ethan morris
#Class: 5th Hour
#Assignment: HW18
import random

#1. Import the "random" library and create a def function that prints "Hello World!"
def hello_world():
    print("Hello World!")
#2. Create a list called beanBag and add at least 5 different colored beans to the list as strings.
beanBag = ["pink", "indigo", "jade", "scarlet", "magenta"]
#3. Create a def function that pulls a random bean out of the beanBag list, prints which bean you pulled, and then removes it from the list.
def pull_random_bean():
    if beanBag:
        pulled_bean = random.choice(beanBag)
        print(f"You pulled a {pulled_bean} bean!")
        beanBag.remove(pulled_bean)
    else:
        print("The beanBag is empty!")

#4. Create a def function that asks if you want to pull another bean out of the bag and, if yes, repeats the #3 def function
def ask_pull_again():
    while beanBag:
        pull_another = input("Do you want to pull another bean? (yes/no): ")
        if pull_another == "yes":
            pull_random_bean()
        elif pull_another == "no":
            print("Thanks for playing!")
            break
        else:
            print(" midinput, please answer with 'yes' or 'no'.")
    if not beanBag:
        print("The beanBag is empty!")
#5. Call the #3 function at the bottom.
pull_random_bean()
