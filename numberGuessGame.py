import random
import pyfiglet

textArt = pyfiglet.figlet_format("Number Guess Game")
print(textArt)
print("I'm thinking of a number between 1 - 100")
print("------------------------------------")

randomNum = random.randint(1, 100)
attemptLeft = 10

chooseDifficulty = input("Choose difficulty: 'easy' or 'hard': ").lower()
print("------------------------------------")
if chooseDifficulty == "hard":
    attemptLeft = 5
    print(f"You have {attemptLeft} attempts left")
    print("------------------------------------")
elif chooseDifficulty == "easy":
    print(f"You have {attemptLeft} attempts left")
    print("------------------------------------")
else:
    print("Invalid input")
    exit()

while attemptLeft > 0:
    guessNum = int(input("Make a guess: "))
    print("------------------------------------")
    if guessNum == randomNum:
        print(f"You Guessed Correctly! The number is {randomNum}")
        print("------------------------------------")
        break
    else:
        attemptLeft -= 1
        print(f"Wrong! You have {attemptLeft} attempts left")
        print("------------------------------------")
        if attemptLeft == 0:
            print("Game over! The number was:", randomNum)
        elif abs(guessNum - randomNum) <= 10 and attemptLeft != 0:
            print("You are close! Guess again")
            print("------------------------------------")
        elif abs(guessNum - randomNum) <= 20 and attemptLeft != 0:
            print("Almost there! Guess again")
            print("------------------------------------")
        else:
            print("Too high! Guess again")
            print("------------------------------------")
