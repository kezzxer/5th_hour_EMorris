import random
import time


class Character:
    def __init__(self, name, health, damage, speed):
        self.name = name
        self.health = health
        self.max_health = health  # max_health attribute
        self.damage = damage
        self.speed = speed

    def take_damage(self, damage):
        """Reduces health by the damage amount."""
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def heal(self, healing_amount):
        """Increases health by the healing amount."""
        self.health += healing_amount
        if self.health > self.max_health:
            self.health = self.max_health

    def damage_over_time(self, damage, duration):
        """Simulates damage over time."""
        for _ in range(duration):
            self.take_damage(damage)
            print(f"{self.name} took {damage} damage. Current health: {self.health}/{self.max_health}")
            time.sleep(1)  # simulate time passing (1 second per tick)


# Create characters based on the values in your request
warrior = Character(name="Warrior", health=100, damage=20, speed=30)
healer = Character(name="Healer", health=80, damage=10, speed=40)
thief = Character(name="Thief", health=50, damage=30, speed=40)
mage = Character(name="Mage", health=45, damage=35, speed=25)

# Put all characters in a list
characters = [warrior, healer, thief, mage]

# Randomly choose a character to apply damage over time
chosen_character = random.choice(characters)
print(f"\nChosen character for damage over time: {chosen_character.name}")

# Apply the damage over time to the chosen character
chosen_character.damage_over_time(damage=5, duration=3)  # Example: 5 damage per second for 3 seconds

# Check who lost health and heal them
if chosen_character.health < chosen_character.max_health:
    print(f"\n{chosen_character.name} has lost health. Healing them...")
    chosen_character.heal(healing_amount=20)  # Example: heal by 20
    print(f"{chosen_character.name}'s health after healing: {chosen_character.health}/{chosen_character.max_health}")
else:
    print(f"\n{chosen_character.name} has full health, no healing needed.")
