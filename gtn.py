import random
import os



guessarray = []
tries = []

print("Guess the random number between 0 and 100! Good luck!") # Initial term

def gameagain(): 
    playagain = input("Do you want to play again? Please, answer with 'y' or 'n'! ")
    if playagain == 'n':
        exit()
    if playagain == "y":
        os.system("python gtn.py")
        print ("Restarting...")
        exit()
 
def checknumber(): # function that work the guesses
    guessinput = input("Your try: ") # input
    if guessinput == '': # if the input.value is undefined, reads '0'
        guessinput = 0
    guess = int(guessinput)
    if guess == value:
        print("You're right! Congratulations!")
        return gameagain()
    if guess > value:
        print("Wrong! Too high")
        guessarray.append(guess) # add the current guess at the guesses list
        print("You guesses was: {}".format(guessarray)) # display the guess list
        tries.append('.') # append on the try list a new dot, to count how many tries i did
        return loopstoper() # call the function that work with the loop
    if guess < value:
        print("Wrong! Too low!")
        guessarray.append(guess)
        print("You guesses was: {}".format(guessarray))
        tries.append('.')
        return loopstoper()


def loopstoper():
    if len(tries) < 10: # check the length of 'tries'. If < 10, you can try again. If not, just the lost label.
        return checknumber()
    if len(tries) == 10: 
        print("You've lost!")
        return gameagain()

value = random.randint(0, 100)
loopstoper()


## loop isn't working