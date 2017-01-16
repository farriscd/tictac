import math
import random
import os
import curses

stdscr = curses.initscr()
curses.curs_set(0)

marks = [0,1,2,
         3,4,5,
         6,7,8]

pos_x = pos_y = 0

def controlK(key):
    global pos_x, pos_y
    if key == 'KEY_DOWN' and pos_y < 4:
        pos_y += 2

    if key == 'KEY_UP' and pos_y > 0:
        pos_y -= 2

    if key == 'KEY_RIGHT' and pos_x < 4:
        pos_x += 2

    if key == 'KEY_LEFT' and pos_x > 0:
        pos_x -= 2

def getPos(y, x):
    if y == 0:
        if x == 0:
            return 0
        if x == 2:
            return 1
        if x == 4:
            return 2
    if y == 2:
        if x == 0:
            return 3
        if x == 2:
            return 4
        if x == 4:
            return 5
    if y == 4:
        if x == 0:
            return 6
        if x == 2:
            return 7
        if x == 4:
            return 8

def showMark(x):
    if x > 8:
        return "x"
    
    if x < 0:
        return "o"
    
    else:
        return " "


def isMarked(x):
    return (showMark(x) == "x" or showMark(x) == "o")


def isWin(X):
    if isMarked(X[0]):
        if showMark(X[0]) == showMark(X[1]) and showMark(X[1]) == showMark(X[2]):
            return True
        if showMark(X[0]) == showMark(X[4]) and showMark(X[4]) == showMark(X[8]):
            return True
        if showMark(X[0]) == showMark(X[3]) and showMark(X[3]) == showMark(X[6]):
            return True
    if isMarked(X[4]):
        if showMark(X[3]) == showMark(X[4]) and showMark(X[4]) == showMark(X[5]):
            return True
        if showMark(X[1]) == showMark(X[4]) and showMark(X[4]) == showMark(X[7]):
            return True
        if showMark(X[2]) == showMark(X[4]) and showMark(X[4]) == showMark(X[6]):
            return True
    if isMarked(X[8]):
        if showMark(X[6]) == showMark(X[7]) and showMark(X[7]) == showMark(X[8]):
            return True
        if showMark(X[2]) == showMark(X[5]) and showMark(X[5]) == showMark(X[8]):
            return True
    else:
        return False

def printBoard(stdscr, X):
    stdscr.addstr(0, 0, "{}|{}|{}".format(showMark(X[0]), showMark(X[1]), showMark(X[2])))
    stdscr.addstr(1, 0, "~|~|~")
    stdscr.addstr(2, 0, "{}|{}|{}".format(showMark(X[3]), showMark(X[4]), showMark(X[5])))
    stdscr.addstr(3, 0, "~|~|~")
    stdscr.addstr(4, 0, "{}|{}|{}".format(showMark(X[6]), showMark(X[7]), showMark(X[8])))

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(5, 0, "Press 'x' to place mark")

    while True:
        printBoard(stdscr, marks)
        
        stdscr.addch(pos_y, pos_x, 'X')
        stdkey = stdscr.getkey()
        controlK(stdkey)
       
        if isWin(marks):
            stdscr.addstr(5, 0, "Computer WINS!              ")
            break
 
        if stdkey == 'x':
            pos = getPos(pos_y, pos_x)
            if isMarked(marks[pos]):
                continue
            marks[pos] = 100

            if isWin(marks):
                stdscr.addstr(5, 0, "You WINS!                ")
                break

            if sum(marks) == 496:
                stdscr.addstr(5, 0, "Cats GAMES!                  ")
                break

            while True:
                com = math.floor(random.random()*9)
                if isMarked(marks[com]):
                    continue
                else:
                    marks[com] = -1
                    break
    
    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)
