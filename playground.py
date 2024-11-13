#Ethan Morris
#5th hour
#playground
print('hey what is your name')
input()
print('are you hungry')
input()
print('you want pasta and i want sandwiches we should flip a coin')
input()
print('heads is pasta and tails is sandwiches, pick heads or tails')
input()
import random
def flip_coin():
  """Flips a coin and returns 'Heads' or 'Tails'."""
  return random.choice(["Heads", "Tails"])
result = flip_coin()
print(result)
print("hooray we finally figured out where to eat")



