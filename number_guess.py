import random

def jibans_guessing_game():

    print("   WELCOME TO JIBAN'S GUESSING GAME ")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")
    # Loop until the player guesses correctly
    while True:
        try:
            # Get player's guess
            guess = input("Enter your guess: ")
            guess = int(guess)
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again. ")
            elif guess > secret_number:
                print("Too high! Try again. ")
            else:
                print(f"\n Awesome job! You beat Jiban's game in {attempts} attempts!")
                break
                
        except ValueError:
            print(" Invalid input! Please enter a valid whole number.")

if __name__ == "__main__":
    jibans_guessing_game()