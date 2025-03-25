#Name:ethan morris
#Class: 5th Hour
#Assignment: HW24

import random, time

#1. Copy over your class from HW23 and all the functions inside of it, and alter any functions to use self if applicable.
class Character:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.max_health = health
        self.damage = damage
        self.speed = speed

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, healing_amount):
        self.health += healing_amount
        if self.health > self.max_health:
            self.health = self.max_health

    def damage_over_time(self, damage, duration):sw
        for _ in range(duration):
            self.take_damage(damage)
            print(f"{self.name} took {damage} damage. Current health: {self.health}/{self.max_health}")
            time.sleep(1)

#2. Create a fourth attribute in the class called max_health that has the same values as health

#3. Copy the warrior and healer objects from HW23, and then make two more character objects with the following attribute values: thief (health/max: 50, damage: 30, speed: 40) and mage (health/max: 45, damage:35, speed: 25)
warrior = Character(name="Warrior", health=100, damage=20, speed=30)
healer = Character(name="Healer", health=80, damage=10, speed=40)
thief = Character(name="Thief", health=50, damage=30, speed=40)
mage = Character(name="Mage", health=45, damage=35, speed=25)
#4. Randomly choose one of the four character objects to take the damage over time function and call the function to them
characters = [warrior, healer, thief, mage]
chosen_character = random.choice(characters)
print(f"\nChosen character for damage over time: {chosen_character.name}")
#5. Determine who lost health by comparing the current health to the max_health and heal that character object by calling your healing function to that object and then print their health afterwards.
chosen_character.damage_over_time(damage=5, duration=3)
if chosen_character.health < chosen_character.max_health:
    print(f"\n{chosen_character.name} has lost health. Healing them...")
    chosen_character.heal(healing_amount=20)
    print(f"{chosen_character.name}'s health after healing: {chosen_character.health}/{chosen_character.max_health}")
else:
    print(f"\n{chosen_character.name} has full health, no healing needed.")