import random

### MAIN MENU ###
def menu():
    try:
        difficulty = int(input("""Please enter a number from the menu to proceed:
        1 - Easy
        2 - Medium
        3 - Hard
        4 - Infernal
        5 - Custom \n"""))
    except ValueError:
        print("Please choose an option from the menu")
        menu()
    if difficulty == 1:
        Easy()
    elif difficulty == 2:
        Medium()
    elif difficulty == 3:
        Hard()
    elif difficulty == 4:
        Infernal()
    elif difficulty == 5:
        custom()
    else:
        print("Please enter a valid number from the menu") # NEED TO CATCH IF USER ENTERS STRING/INVALID INPUT

## CHECK GUESS ##
def check(guess, number):
    correct_msg = "You guessed correctly!"
    low_msg = "Your guess is too low"
    high_msg = "Your guess is too high"
    
    if guess == number:
        return correct_msg
    elif guess < number:
        return low_msg
    elif guess > number:
        return high_msg        

## REPLAY SELECTION ##   
def play_again():
    play = int(input("To return to the menu press 1, to exit press 2\n"))
    if play == 1:
        print("--------------------")
        menu()
    elif play == 2:
        exit()
    else:
        print("Please enter a valid number from the menu")
        
### DIFFICULTY SETTINGS ###
def Easy():
    print("--------------------")
    print("""Easy mode selected.\nattempts = +20.\nThe number is between 1 and 30\nGood Luck!\n""")
## SET VARIABLES ##
    counter = 0
    number = random.randint(1,30)
## GAME LOOP ##
    while counter < 20:
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Please enter a valid guess")
            continue
        checking = check(guess, number)
        if checking == "You guessed correctly!":
            print(checking)
            play_again()
        elif checking == "Your guess is too low" or "Your guess is too high":
            print(checking)
            counter = counter + 1
            print(f"You have {20 - counter} attempts left\n")
    if counter == 20:
        print("You have run out of attempts, better luck next time!")
        print(f"The number was {number}")
        play_again()

def Medium():
    print("--------------------")
    print("""Medium mode selected.\nattempts = +15.\nThe number is between 1 and 50\nGood Luck!""")
## SET VARIABLES ##
    counter = 0
    number = random.randint(1,50)
## GAME LOOP ##
    while counter < 15:
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Please enter a valid guess")
            continue
        checking = check(guess, number)
        if checking == "You guessed correctly!":
            print(checking)
            play_again()
        elif checking == "Your guess is too low" or "Your guess is too high":
            print(checking)
            counter = counter + 1
            print(f"You have {15 - counter} attempts left\n")
    if counter == 15:
        print("You have run out of attempts, better luck next time!")
        print(f"The number was {number}")
        play_again()

def Hard():
    print("--------------------")
    print("""Hard mode selected.\nattempts = +10.\nThe number is between 1 and 50\nGood Luck!""")
## SET VARIABLES ##
    counter = 0
    number = random.randint(1,50)
## GAME LOOP ##
    while counter < 10:
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Please enter a valid guess")
            continue
        checking = check(guess, number)
        if checking == "You guessed correctly!":
            print(checking)
            play_again()
        elif checking == "Your guess is too low" or "Your guess is too high":
            print(checking)
            counter = counter + 1
            print(f"You have {10 - counter} attempts left\n")
    if counter == 10:
        print("You have run out of attempts, better luck next time!")
        print(f"The number was {number}")
        play_again()

def Infernal():
    print("--------------------")
    print("""Infernal mode selected.\nattempts = +5.\nThe number is between 1 and 100\nGood Luck!""")
## SET VARIABLES ##
    counter = 0
    number = random.randint(1,100)
## GAME LOOP ##
    while counter < 5:
        try:
            guess = int(input("Please enter your guess: "))
        except ValueError:
            print("Please enter a valid guess")
            continue
        checking = check(guess, number)
        if checking == "You guessed correctly!":
            print(checking)
            play_again()
        elif checking == "Your guess is too low" or "Your guess is too high":
            print(checking)
            counter = counter + 1
            print(f"You have {5 - counter} attempts left\n")
    if counter == 5:
        print("You have run out of attempts, better luck next time!")
        print(f"The number was {number}")
        play_again()

def custom():
    print("--------------------")
    print("""Custom mode selected.\n""")
    print("In this mode you are able to set the range in which a number can be generated in")
    print("Also you will set the number of guesses you will recieve")
## SET VARIABLES ##
    try:
        counter = int(input("Please enter the number of guesses you would like to have: "))
    except ValueError:
        print("Please enter a valid number")
        custom()
    

# Main
print("Hello and welcome to the Number Guessing Game.\nAs you can imagine the idea is thatnyou have to try and guess a randomly\ngenerated number within a certain amount of attempts\n")
print("This game has 4 difficulty modes ~ \nEasy | Medium | Hard | Infernal.\n")
print("There is also an option to create a custom game mode.\n")
menu()
    