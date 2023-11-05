import random

### MAIN MENU ###
def menu():
    difficulty = int(input("""Please enter a number from the menu to proceed:
    1 - Easy
    2 - Medium
    3 - Hard
    4 - Infernal \n"""))

    if difficulty == 1:
        Easy()
    elif difficulty == 2:
        Medium()
    elif difficulty == 3:
        Hard()
    elif difficulty == 4:
        Infernal()
    else:
        print("Please enter a valid number from the menu") # NEED TO CATCH IF USER ENTERS STRING/INVALID INPUT

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
    print("""Easy mode selected.\nattempts = +20.\nThe number is between 1 and 30\nGood Luck!""")
## SET VARIABLES ##
    counter = 0
    number = random.randint(1,30)
## GAME LOOP ##
    while counter < 20:
        guess = int(input("Please enter your guess: "))

def Medium():
    print("--------------------")
    print("""Medium mode selected.\nattempts = +15.\nThe number is between 1 and 50\nGood Luck!""")
## SET VARIABLES ##
    counter = 0
    number = random.randint(1,50)
## GAME LOOP ##
    while counter < 15:
        guess = int(input("Please enter your guess: "))


def Hard():
    print("--------------------")
    print("""Hard mode selected.\nattempts = +10.\nThe number is between 1 and 50\nGood Luck!""")
## SET VARIABLES ##
    counter = 0
    number = random.randint(1,50)
## GAME LOOP ##
    while counter < 10:
        guess = int(input("Please enter your guess: "))




def Infernal():
    print("--------------------")
    print("""Infernal mode selected.\nattempts = +5.\nThe number is between 1 and 100\nGood Luck!""")
## SET VARIABLES ##
    counter = 0
    number = random.randint(1,100)
## GAME LOOP ##
    while counter < 5:
        guess = int(input("Please enter your guess: "))
        

# Main
print("Hello and welcome to the Number Guessing Game.\nAs you can imagine the idea is thatnyou have to try and guess a randomly\ngenerated number within a certain amount of attempts\n")
print("This game has 4 difficulty modes ~ \nEasy | Medium | Hard | Infernal.\n")
menu()
    