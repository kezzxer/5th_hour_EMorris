#Name:ethan morris
#Class: 5th Hour
#Assignment: HW22

#1. Create a class containing a def function that inits self and 3 other attributes for store items (stock, cost, and weight).
class StoreItem:
    def __init__(self, stock, cost, weight):
        self.stock = stock
        self.cost = cost
        self.weight = weight

    def double_cost(self):
        self.cost *= 2
#2. Make 3 objects to serve as your store items and give them values to those 3 attributes defined in the class.
doomgauntlet  = StoreItem(5, 115.99, 11.2)
Frayedblade = StoreItem(1, 20000, 22.5)
soulofdarkeatermidir = StoreItem(100, 5.99, 0.8)
#3. Print the stock of all three objects and the cost of the second store item.
print(f"Stock of Item 1: {doomgauntlet.stock}")
print(f"Stock of Item 2: {Frayedblade.stock}")
print(f"Stock of Item 3: {soulofdarkeatermidir.stock}")
print(f"Cost of Item 2: ${Frayedblade.cost}")
#4. Make a def function within the class that doubles the cost an item, double the cost of the second store item, and print the new cost below the original cost print statement.
Frayedblade.double_cost()
print(f"New cost of Item 2: ${Frayedblade.cost}")
#5. Directly change the stock of the third store item to approx. 1/4th the original stock and then print the new stock amount.
soulofdarkeatermidir.stock = int(soulofdarkeatermidir.stock / 4)
print(f"New stock of Item 3: {soulofdarkeatermidir.stock}")
#6. Delete the first store item and then attempt to print the weight of the first store item. Create a try/except catch to fix the error.
del doomgauntlet
try:
    print(f"Weight of Item 1: {doomgauntlet.weight}")
except NameError as e:
    print(f"Error: {e}. Item 1 has been deleted.")
