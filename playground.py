#Ethan Morris
#5th hour
#playground
#print('hey what is your name')
#input()
#print('are you hungry')
#input()
#print('you want pasta and i want sandwiches we should flip a coin')
#input()
#print('heads is pasta and tails is sandwiches, pick heads or tails')
#input()
import random
def flip_coin():

  return random.choice(["Heads", "Tails"])
result = flip_coin()
print(result)
print("hooray we finally figured out where to eat")


def add(a, b):
  return a + b


result = add(3, 5)  # Returns 8


def greet(name, greeting="Hello"):
  return f"{greeting}, {name}!"


print(("ryleigh says greetings huzz "))
print(greet("ethan", "Good morning"))



