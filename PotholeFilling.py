"""
File: PotholeFilling.py
Name: TODO:
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
def turn_right():
    """
    pre-condition:karel is at(2,1),facing east
    post-condition:karel is at(2,7),facing east
    """
    turn_left()
    turn_left()
    turn_left()



def go_in():
    """
    pre-condition:karel is at(2,1),facing east
    post-condition:karel is at(2,7),facing east
    """
    move()
    turn_right()
    move()
    for i in range(99):
       put_beeper()
def go_out():
    """
    pre-condition:karel is at(2,1),facing east
    post-condition:karel is at(2,7),facing east
    """
    turn_left()
    turn_left()
    move()
    turn_right()
    move()


def main():
    """
    pre-condition:karel is at(2,1),facing east
    post-condition:karel is at(2,7),facing east
    """
    for i in range(3):
       go_in()
       go_out()







# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
