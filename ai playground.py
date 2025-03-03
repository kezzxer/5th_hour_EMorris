import random

# List of 5-letter words for the game
WORD_LIST = ["apple", "grape", "peach", "mango", "zebra", "melon", "lemon", "berry", "plaza", "vivid"]


# Function to give feedback on the guess
def give_feedback(secret_word, guess):
    feedback = []

    # Create a list of characters from the secret word to track already used characters
    secret_word_list = list(secret_word)

    # First pass: Check for correct letters in the correct position (Green)
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            feedback.append("🟩")  # Green square
            secret_word_list[i] = None  # Mark this position as already matched
        else:
            feedback.append(None)

    # Second pass: Check for correct letters in the wrong position (Yellow)
    for i in range(len(guess)):
        if feedback[i] is None and guess[i] in secret_word_list:
            feedback[i] = "🟨"  # Yellow square
            secret_word_list[secret_word_list.index(guess[i])] = None  # Mark the character as used

    # Third pass: Letters that are not in the word at all (Gray)
    feedback = [f if f is not None else "⬛" for f in feedback]  # Gray square

    return "".join(feedback)


# Main game function
def wordle():
    # Choose a random word from the list
    secret_word = random.choice(WORD_LIST)
    attempts = 6

    print("Welcome to Wordle!")
    print("Try to guess the 5-letter word. You have 6 attempts.")

    # Start the game loop
    for attempt in range(attempts):
        print(f"\nAttempt {attempt + 1}/{attempts}")

        # Get user's guess
        guess = input("Enter your guess: ").lower()

        if len(guess) != 5:
            print("Please enter a 5-letter word.")
            continue

        # Check if guess is correct
        if guess == secret_word:
            print("Congratulations! You've guessed the word!")
            break

        # Provide feedback
        feedback = give_feedback(secret_word, guess)
        print(f"Feedback: {feedback}")

        # If all attempts are used
        if attempt == attempts - 1:
            print(f"Sorry, you've run out of attempts! The secret word was: {secret_word}")


if __name__ == "__main__":
    wordle()

