#Name: ethan m & kevin z
#Class: 5th Hour
#Assignment: Scenario 5

#Scenario 5
#You're all part of a new development team and the big wigs want to see what you are all capable of.
#They want you to develop whatever you want to develop, but there's only one problem:
#the same big wigs only bought enough computers for half of you. Because of this, you will
#all be split into teams of two. One serving as the brain (not using the computer),
#one serving as the hands (using the computer).

#The Teams are as such:

#Team 1: Dom (brain), Zachary (hand)
#Team 2: Ryley (brain), Ethan W (hand)
#Team 3: Eli (brain), Preston (hand)
#Team 4: Gabe (brain), Quinn (hand)
#Team 5: Sam (brain), Chaysen (hand)
#Team 6: Kevin (brain), Ethan M (hand)
#Team 7: Gage (brain), Eric (hand)


#You have until the Scenario is due to brainstorm an idea together, create a flowchart, and then
#turn that flowchart into functioning code. The code itself must have at least: 1 dictionary or list,
#1 loop, 2 if statements (elif and else statements tied to it does not count towards the total),
#1 variable with a user input, and 1 form of an assignment operator. You are free to add whatever else
#you feel is necessary to complete your concept. You will be graded based on how those ideas are
#implemented together.

import random

print("Welcome to the Overwatch Loot Box Simulator!")


lootboxes = int(input("Please enter the number of lootboxes: "))


OverwatchSkins = [
    'Legendary: Oni Genji',
    'Epic: Frostbite Pharah',
    'Rare: Banana Winston',
    'Rare: Cobalt Reinhardt',
    'Epic: Synaesthesia Lucio',
    'Legendary: Lone Wolf Hanzo',
    'Rare: Rose Widowmaker',
    'Rare: Celestial Mercy',
    'Epic: Carbon Fiber D.VA',
    'Legendary: Dr. Junkenstein Junkrat',
    'Epic: Nihon Genji',
    'Rare: Blood Reaper',
    'Rare: Ebony McCree',
    'Epic: Demon Hanzo',
    'Rare: Peridot Ana',
    'Rare: Lemonlime D.VA',
    'Epic: Taegeukgi D.VA',
    'Legendary: Mei-rry Mei',
    'Legendary: Augmented Sombra',
    'Rare: Technomancer Symmetra',
    'Rare: Mud Roadhog'
]


if lootboxes == 0:
    print("No more boxes!")
    quit()


while lootboxes > 0:
    OpenBox = input("Type 'open' to open a loot box: ")

    if OpenBox.lower() == "open":
        print(random.choice(OverwatchSkins))
        lootboxes -= 1
        print(f"Boxes left: {lootboxes}")
    else:
        print("Invalid input. Please type 'open' to open a loot box.")

print("No more lootboxes to open! Thanks for playing.")




