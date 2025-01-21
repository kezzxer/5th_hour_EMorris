#Name:ethan morris
#Class: 5th Hour
#Assignment: Scenario 4

#Scenario 4:
#Due to scope creep leading to high development costs, the RPG you were working on has been
#shelved for the time being. You have been transferred to a new team working on a mobile game
#that allows you to dress up a model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score all the ratings.
print("Hello, Welcome to Dress to Impress")
def rate_model():
    num_players = int(input("Enter the number of players: "))

    ratings = []
    for i in range(1, num_players + 1):
        while True:
            try:
                rating = int(input(f"Player {i}, enter your rating (1-5): "))
                if 1 <= rating <= 5:
                    ratings.append(rating)
                    break
                else:
                    print("wrong rating. Please enter a number between 1 and 5.")
            except ValueError:
                print(" wrong input. Please enter a number.")

    print("Ratings:", ratings)

rate_model()
rating = [2,3,5,1,2]
average_rating = sum(rating) / len(rating)
print(average_rating)
