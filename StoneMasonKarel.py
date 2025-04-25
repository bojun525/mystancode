"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *
def go():
   while front_is_clear():
       if not on_beeper():
          put_beeper()
          move()
       else:
           move()
   if on_beeper():
       turn()
   else:
       put_beeper()
       turn()

def goo():
    while front_is_clear():
       if not on_beeper():
          put_beeper()
          move()
       else:
          move()
    if on_beeper():
        turrn()
    else:
        put_beeper()
        turrn()

def turn_right():
    turn_left()
    turn_left()
    turn_left()




def move_four():
    move()
    move()
    move()
    move()
def turn():
        turn_right()
        move_four()
        turn_right()
def turrn():
    if not front_is_clear():
        turn_left()
        move_four()
        turn_left()




def main():
   turn_left()
   for i in range(2):
    go()
    goo()




# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
