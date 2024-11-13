
#Name: Ethan Morris
#Class: 5th Hour
#Assignment: HW10
import time
#1. Create a while loop with variable i that counts down from 5 to 0
#and then prints "Hello World!" at the
j = 5
while j >= 0:
    print(j)
    time.sleep(1)
    j -= 1
else:
    print("hello world")
#2. Create a while loop that prints only even numbers
#between 1 and 30.
j=30
while j >= 0:
    print(j)
    time.sleep(2)
    j -= 2
#3. Create a while loop that repeats until the user
#inputs the number 0
n = int(input("pick a number"))
while n!=0:
    print(n)
    n = int(input("pick another number"))