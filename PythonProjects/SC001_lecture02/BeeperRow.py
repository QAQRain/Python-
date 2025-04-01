"""
File: BeeperRow.py
Name: QAQrain
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *

from MoveToTheEnd import *

def main():
    put()
    while front_is_clear():
        m()
        put()


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
