import random

print('---------------------------------------------------')
print('              GUESS THE NUMBER APP')
print('---------------------------------------------------\n')

answer = random.randint(1, 100)

print("I've guessed a number between 1 and 100. Think you can guess it?")

while True:
    guess = int(input('What is your guess? '))
    if guess == answer:
        print("That's correct.  You're a WIENER!!!")
        exit(0)
    elif guess > answer:
        print('That guess is too high! Guess again! ')
        continue
    else:
        print('That guess is too low! Guess again! ')
        continue
