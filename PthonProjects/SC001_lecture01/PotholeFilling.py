"""
File: PotholeFilling.py
Name: QAQrain
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
from StepUp import *

def m():
    move()

def tl():
    turn_left()

def tr():
    for i in range(3):
        turn_left()

def tb():
    for i in range(2):
        tr()

def pick():
    pick_beeper()

def put():
    put_beeper()

def put99():
    for i in range(99):
        put_beeper()

def go_in():
	"""
	precondition:K at 2,1 Face E
	pothcondition:K at 2,7 Face E and fill three hole with 99 beepers
	"""

def go_out():
	"""
	precondition:K at 2,7 Face E and fill three hole with 99 beepers
	pothcondition"K at 2,1 Face E
	"""

def main():

    for i in range(3):
        m()
        tr()
        m()
        put99()
        tb()
        m()
        tr()
        m()

# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
