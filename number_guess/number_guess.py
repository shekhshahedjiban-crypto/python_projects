import random #random module is imported to generate random numbers

def jibans_guessing_game(): #function to run jiban's guessing game

    print("   WELCOME TO JIBAN'S GUESSING GAME ") #print welcome message for the game
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100) #randint function is used to generate a random number between 1 and 100
    attempts = 0 #attempts variable is initilized to keeptrack of the number of attempts made by the player
    
    print("I'm thinking of a number between 1 and 100.") #print message to inform the player about the range of the secret number
    print("Can you guess what it is?") #ask the player if they can guess the secret number
    # Loop until the player guesses correctly
    while True:
        try:
            # Get player's guess
            guess = input("Enter your guess: ")
            guess = int(guess) #convert the input to an integer to check if the guess is a valid whole number
            attempts += 1

            # Checking the guess 
            if guess < secret_number: #if the guess is less than the secret number,print a messsage to inform the player that their guess is too low
                print("Too low! Try again. ")
            elif guess > secret_number:
                print("Too high! Try again. ") #if the guess is greater than the secret number,print a message to inform the player that their guess is too high
            else:
                print(f"\n Awesome job! You beat Jiban's game in {attempts} attempts!") #if theguess is equal to the secret number,print a message to inform that the player has guessed the number correctly and displays the attempts made by the player 
                break #break the loop if the player has guessed the number correctly
                
        except ValueError: #if input is not a valid whole number then it will raise valueerror and the except block will be executed to handle the error and print an error messaage 
            print(" Invalid input! Please enter a valid whole number.")

if __name__ == "__main__": #__name__ =="__main--" is used in python to check if the script is being run directly or imported
    jibans_guessing_game() #call the function to start the game
