import random


class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def attack(self, target):
        # Simulate a d20 attack roll
        attack_roll = random.randint(1, 20)
        print(f"Attack roll: {attack_roll}")

        # Calculate if the attack hits (we assume an arbitrary target defense of 10)
        hit = attack_roll + self.damage > 10  # We assume the target defense is 10 for simplicity

        if hit:
            print(f"{self.__class__.__name__} hits {target.__class__.__name__} for {self.damage} damage!")
            target.health -= self.damage
        else:
            print(f"{self.__class__.__name__} misses {target.__class__.__name__}.")

    def is_alive(self):
        return self.health > 0


# Creating characters with random damage values
Shadowheart = Character(12, random.randint(1, 6) + random.randint(1, 6) + 3, 30)
Gale = Character(8, random.randint(1, 6) + 3, 30)
LaeZel = Character(10, random.randint(1, 10), 30)
Astarion = Character(10, random.randint(1, 6) + 4, 30)
genji = Character(8, random.randint(1, 6) + 4, 30)
lilyachty = Character(8, random.randint(1, 6) + 4, 30)
travisscott = Character(8, random.randint(1, 6) + 4, 30)
drake = Character(8, random.randint(1, 6) + 4, 30)

# Example of an attack roll
Shadowheart.attack(Gale)
print(f"Gale's remaining health: {Gale.health}")
