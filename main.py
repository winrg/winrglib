import curses


#init curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
curses.curs_set(0)
curses.start_color()

#init the screen
stdscr = curses.initscr()
stdscr.keypad(True)
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
stdscr.bkgd(curses.color_pair(1))
stdscr.timeout(42)

#the stuff that the function takes in as inputs
xpos = 1
ypos = 1
options = [['upgrade 1', '10', 490, 'get1'], 
          ['upgrade 2', '20', 500, 'get2'], 
          ['upgrade 3', '30', 510, 'get3'], 
          ['prestige', '100', 80, 'getp']]
height = 20
width = 20
exitkey = 120



class menu:
  def __init__(self, dimensions: tuple, 
