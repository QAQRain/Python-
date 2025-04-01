"""
File: MoveToTheEnd.py
Name: QAQrain
------------------------
This file shows how to use while loop
to walk to the end of a certain row in
karel world
"""

from karel.stanfordkarel import *


def m():
    move()

def tl():
    turn_left()

def tr():
    for i in range(3):
        turn_left()

def pick():
    pick_beeper()

def put():
    put_beeper()

def main():
    """
    Karel will move to the end of the first Street in any world
    """
    while front_is_clear():
        m()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
