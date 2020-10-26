answer = 23

attempts = 0

entry = ""

''' a loop that repeats while the users guess isn't the same as the answer '''

print("\n\t\t Guess the Number - Game")


while answer != entry :

    entry = int(input("\n\t   Enter a number between 1 and 100 : "))
    
    ''' Each time through the loop 1 is added to the number of attempts '''
    
    attempts = attempts + 1
    
''' After the loop it will say how many attempts it took '''

print("\nWell done you correctly guessed the number it took you " + str(attempts) + " attempts")
