#Ethan Morris
#5th hour
#playground
#https://www.google.com/search?q=how+to+flip+a+coin+with+python&sca_esv=9102e70e77a48ac0&ei=kfDZZuOWH_CYkPIPmJGq6QE&ved=0ahUKEwijo6H4r6yIAxVwDEQIHZiIKh0Q4dUDCBA&uact=5&oq=how+to+flip+a+coin+with+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiHmhvdyB0byBmbGlwIGEgY29pbiB3aXRoIHB5dGhvbjIGEAAYFhgeMgsQABiABBiGAxiKBTILEAAYgAQYhgMYigUyCxAAGIAEGIYDGIoFMggQABiABBiiBDIIEAAYogQYiQUyCBAAGIAEGKIEMggQABiABBiiBEieK1CYI1jSJ3ABeAGQAQCYAW6gAe0CqgEDMy4xuAEDyAEA-AEBmAIFoAKUA8ICChAAGLADGNYEGEeYAwCIBgGQBgiSBwM0LjGgB8gY&sclient=gws-wiz-serp
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