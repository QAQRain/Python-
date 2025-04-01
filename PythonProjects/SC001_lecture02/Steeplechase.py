"""
File: Steeplechase.py
Name: QAQrain
---------------------------------
"""

from karel.stanfordkarel import *

from MoveToTheEnd import  *

def jump():
    up()
    cross()
    down()

def up():
    while not right_is_clear():
        if front_is_clear():
            move()

def cross():
    tr()
    m()
    tr()

#   Way1
def down():
    while front_is_clear():
        move()
    if not front_is_clear():
        turn_left()

#   Way2
# def down():
#     while front_is_clear():
#         move()
#     if not front_is_clear():
#         turn_left()
#         if not front_is_clear():
#             turn_left()
#             jump()

def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
#   Way1
    for i in range(3):
        while front_is_clear():
            m()
            if not front_is_clear():
                turn_left()
                jump()
        if not front_is_clear():
            turn_left()
            jump()

#   Way2
#     while front_is_clear():
#         m()
#         if not front_is_clear():
#             turn_left()
#             jump()

"""
ps:
there is two way to done this work
The Way1 is better to End because it will stop when it done the last jump.
But it can't do jump for infinite.
So I did another way.
The Way2 can detect it need do jump after did a jump or not.
And it can cross all the obstacles forever.
"""


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
