#Name:ethan morris
#Class: 5th Hour
#Assignment: Scenario8

import random
#Scenario 8:
#With a fresh perspective, the team lead wants you to look back and refactor the old combat code to
#be streamlined with classes so the character and enemy stats won't be built in bulky dictionaries anymore.

#(Translation: Rebuild Scenario 3 using classes instead of dictionaries, include the combat test code
#below as well.)
import random


class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def attack(self, target):

        attack_roll = random.randint(1, 20)
        print(f"Attack roll: {attack_roll}")


        hit = attack_roll + self.damage > 10

        if hit:
            print(f"{self.__class__.__name__} hits {target.__class__.__name__} for {self.damage} damage!")
            target.health -= self.damage
        else:
            print(f"{self.__class__.__name__} misses {target.__class__.__name__}.")

    def is_alive(self):
        return self.health > 0



Shadowheart = Character(12, random.randint(1, 6) + random.randint(1, 6) + 3, 30)
Gale = Character(8, random.randint(1, 6) + 3, 30)
LaeZel = Character(10, random.randint(1, 10), 30)
Astarion = Character(10, random.randint(1, 6) + 4, 30)
genji = Character(8, random.randint(1, 6) + 4, 30)
lilyachty = Character(8, random.randint(1, 6) + 4, 30)
travisscott = Character(8, random.randint(1, 6) + 4, 30)
drake = Character(8, random.randint(1, 6) + 4, 30)


Shadowheart.attack(Gale)
print(f"Gale's remaining health: {Gale.health}")

