"""
File: guess_my_number.py
Name:
-----------------------------
This program plays a Console game
"Guess My Number" which asks user
to input a number until he/she gets it
"""

# This number controls when to stop the game
SECRET = 32


def main():
    for i in range(50):
     print('guess0-99')
     guess=int(input('your guess?'))
     if True:
           if guess == SECRET:
            print('congrats,' + str(guess) + '!')
           elif guess < SECRET:
            print('too low')
           elif guess > SECRET:
            print('too high')






# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    main()
