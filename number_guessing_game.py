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
        if guess == number:
            print(f"Congratulations! You guessed the number in {counter} attempts")
            break
        elif guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        counter += 1
    else:
        print(f"You have run out of attempts, the number was {number}\n")
## PLAY AGAIN ##
    play = int(input("To return to the menu press 1, to exit press 2\n"))
    if play == 1:
        print("--------------------")
        menu()
    elif play == 2:
        exit()
    else:
        print("Please enter a valid number from the menu") 

def Medium():
    print("--------------------")

def Hard():
    print("--------------------")

def Infernal():
    print("--------------------")


# Main
print("""Hello and welcome to the Number Guessing Game, as you can imagine the idea is that you have to
try and guess a randomly generated number within a certain amount of attempts
This game has 4 difficulty modes ~ Easy | Medium | Hard | Infernal.\n""")
menu()
    