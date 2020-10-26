''' Coursera Guided Project : Introduction to Python '''

''' User's will input/provide Guess Number '''

import random

def AIGuess(highval,lowval,randnum, count=0):

    if highval >= lowval:
        guess = lowval +(highval - lowval) // 2

        ''' if  guess is found in the Middle, It is found! if Guess is greather than the number It must be found in the lower half of a number between lower value and the guess. number must be in the uper set of numbers the guess and the upper value '''

        if guess == randnum:
            return count

        elif guess > randnum:
            count = count + 1
            return AIGuess(lowval,guess-1,randnum,count)

        else:
            count = count + 1
            return AIGuess(guess + 1, highval, randnum, count)

    else:
        ''' Number Not Found '''

        return -1
    ''' End of Function '''

''' Generate Random Number from 1 to 100 '''
randnum = random.randint(1,101)

count = 0
guess = -99

''' Decison Construct's '''
while (guess != randnum):

    ''' Get the User's Guess '''
    guess = int(input("\t\t Provide your Guess Value Bwtween(B/W) 1 and 100: "))

    if guess < randnum:
        print("Higher")

    elif guess > randnum:
        print("Lower")

    else:
        print("You Guessed It")
        break

    count = count + 1

print("You Took "+ str(count) + "Steps to guess the number")

print("AI Took "+ str(AIGuess(0,100, randnum)) +"step!")



