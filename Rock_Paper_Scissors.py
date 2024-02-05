from getpass import getpass 

#The Winner function compares both player inputs and outputs who won
def Winner(player1choice, player2choice, user1, user2):
    if player1choice == player2choice:
        return "It's a tie!"
    elif player1choice in ['ROCK', 'rock']:
        if player2choice in ['SCISSORS', 'scissors']:
            return "ROCK wins!\nCongratulations, " + user1 + "!"
        elif player2choice in ['PAPER', 'paper']:
            return "PAPER wins!\nCongratulations, " + user2 + "!"
        else:
            return "Sorry! Someone didn't choose one of the three choices... Try again!"
    elif player1choice in ['SCISSORS', 'scissors']:
        if player2choice in ['PAPER', 'paper']:
            return "SCISSORS wins!\nCongratulations, " + user1 + "!"
        elif player2choice in ['ROCK', 'rock']:
            return "ROCK wins!\nCongratulations, " + user2 + "!"
        else:
            return "Sorry! Someone didn't choose one of the three choices... Try again!"
    elif player1choice in ['PAPER', 'paper']:
        if player2choice in ['ROCK', 'rock']:
            return "PAPER wins!\nCongratulations, " + user1 + "!"
        elif player2choice in ['SCISSORS', 'scissors']:
            return "SCISSORS wins!\nCongratulations, " + user2 + "!"
        else:
            return "Sorry! Someone didn't choose one of the three choices... Try again!"
    else:
        return "Whoops! Try again, but this time please make sure to select one of the three choices: ROCK, PAPER, or SCISSORS!"


while True:
    #Basic introduction
    print("\nWelcome to Rock, Paper, Scissors!")
    #Rules of the game
    print("\n          RULES        ")
    print("**************************")
    print("** ROCK beats SCISSORS  **")
    print("** PAPER beats ROCK     **")
    print("** SCISSORS beats PAPER **")
    print("**************************")

    #Prompts both players for their names and assigns them a player number
    user1 = input("\n\nWhat's your name? ")
    print("Player 1 will be:", user1)
    user2 = input("\nWhat's your name? ")
    print("Player 2 will be:", user2)

    player1choice = getpass("\nPlayer 1's turn: ") #Hides the Player 1 selection
    player2choice = getpass("Player 2's turn: ") #Hides the Player 2 selection


    player1choice = player1choice.upper() #Reads in every entry for Player 1 into uppercase
    player2choice = player2choice.upper() #Reads in every entry for Player 2 into uppercase

    #Declares a showdown between two choices, in order by player number
    print("\n\nIn today's showdown we have", player1choice, "VS", player2choice+"!!!\n")

    # Calls the Winner function to determine a winner of the showdown
    print(Winner(player1choice, player2choice, user1, user2))

    #Prompts the user if they would like to play again
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break