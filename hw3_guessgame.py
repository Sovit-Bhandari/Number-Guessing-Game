'''Name = Sovit Bhandari
U-number= U83561265
Brief discription = The following code is used for the guessing game where the computer generate a 
random number for user to guess. This code only allow 10 attempts for the user to guess the number.'''

import random
EntNum = int(input('Enter a number between 1 and 100(inclusive):'))
guess = list(range(1,101))                                                              #creating the list for computer to generate random number
GuessedNum = random.choice(guess)
attempt = 1
while attempt<=9:                                                                       #providing the user 10 attempts guess
    if EntNum>100:          
        EntNum = int(input('Very Funny. Enter a number between 1 and 100(inclusive):'))
    if EntNum<0:
        EntNum = int(input('Really? Enter another guess between 1 and 100:'))
    #creating the conditions for user choice with the computer choice
    if EntNum==GuessedNum:
        print(f'You guessed it right!! You got it in {attempt} guesses!')
        break                                                                           #terminating the game if guessed right
    if EntNum>GuessedNum:
        EntNum = int(input('Too high. Enter another guess:'))
    elif EntNum<GuessedNum:
        EntNum = int(input('Too low. Enter another guess:'))
    attempt = attempt +1
else:                                                                                   #If user couldn't guess in all 10 attempts
    print(f"Sorry the number was {GuessedNum}")
