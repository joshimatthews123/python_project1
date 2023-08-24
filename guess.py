import random

name = input("Enter Your name? ")

print(f"Hi {name}, whould you like to play? ")

userIntrest = input("Enter your intrest? ").lower()


def gameOn():
    rangeNumber = input("Enter a num, how much range do you want? ")

    if rangeNumber.isdigit():
        rangeNumber = int(rangeNumber)
        randomNumber = random.randint(1, rangeNumber)
        count = 1

        while True:
            guessNumber = input(f"Guess a number between 1, {rangeNumber} ")
            if guessNumber.isdigit():
                if int(guessNumber) == randomNumber:
                    print(
                        f"Yo {name},You guessed a number in {count} times, You did it :) "
                    )
                    break
                elif int(guessNumber) != randomNumber:
                    count += 1
                    print("Please guess correct number...")
                    continue


if userIntrest != "yes":
    print("Are you sure, quit the game? yes or no")
    userIntrest = input("Enter Y/N ").lower()
    if userIntrest == "y":
        print(f"ok {name}, Good Bye :) ")
        quit()
    elif userIntrest == "n":
        gameOn()
