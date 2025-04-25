"""
File: Steeplechase.py
Name: gary －ㄉ 
---------------------------------
pre-condition:Karel is at (1,1),facing east
post-condition:Karel is at (12,1),facing east
"""

from karel.stanfordkarel import *

def turn_right():
    """
    pre - condition: Karel is at(1, 1), facing east
    post - condition: Karel is at(12, 1), facing east
    """
    turn_left()
    turn_left()
    turn_left()



def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop
    pre-condition:Karel is at (1,1),facing east
    post-condition:Karel is at (12,1),facing east
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            up()
            down()
def up():
    """
    pre - condition: Karel is at(1, 1), facing
    east
    post - condition: Karel is at(12, 1), facing
    east
    """
    while not front_is_clear():
        turn_left()
        move()
        turn_right()

def down():
    """
        pre - condition: Karel is at(1, 1), facing
        east
        post - condition: Karel is at(12, 1), facing
        east
    """
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
