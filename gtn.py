from random import seed
from random import randint

seed(1)

guessarray = []

print("Guess the random number between 0 and 100! Good luck!") # Initial term

def checknumber(): # function that work the guesses
    guess = int(input("Your try: ")) # input
    if guess == value:
        print("Right")
    if guess > value:
        print("Wrong! Too high")
        guessarray.append(guess) # add the current guess at the guesses list
        print("You guesses was: {}".format(guessarray)) # display the guess list
        return loopstoper() # call the function that work with the loop
    if guess < value:
        print("Wrong! Too low!")
        guessarray.append(guess)
        print("You guesses was: {}".format(guessarray))
        return loopstoper()


def loopstoper():
    tries = 0
    if tries < 10:
        return checknumber()
    else: 
        print("You've lost!")
    print(tries)

value = randint(0, 100)
print(value)
loopstoper()

## loop isn't working