#Name:ethan morris
#Class: 5th Hour
#Assignment: HW21


#1. Make a nested dictionary with three entries called "sport1", "sport2", and "sport3" containing
#the name a sport the school partakes in, the amount of players a typical team uses during gameplay
#(ex: Basketball has 5 players), and if the sport uses a ball or not (as a boolean).
sports = {
    "sport1": {
        "name": "Basketball",
        "players": 5,
        "uses_ball": True
    },
    "sport2": {
        "name": "Soccer",
        "players": 11,
        "uses_ball": True
    },
    "sport3": {
        "name": "Volleyball",
        "players": 6,
        "uses_ball": True
    }
}
#2. Create a def function that pulls the values from the dictionary as arguments, adds together the
#players of all three sports, and prints the sum
def total_players(sport1_players, sport2_players, sport3_players):
    total = sport1_players + sport2_players + sport3_players
    print("Total players across all sports:", total)
#3. Call the function with arguments here
total_players(sports["sport1"]["players"], sports["sport2"]["players"], sports["sport3"]["players"])