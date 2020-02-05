import curses
from time import sleep
from numpy import mod

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
poss = (1, 1)
optionss = [['upgrade 1', 10, 49, 'get1'], 
          ['upgrade 2', 20, 50, 'get2'], 
          ['upgrade 3', 30, 51, 'get3'], 
          ['prestige', 100, 80, 'getp']]
dimensionss = (20, 21)
exitkey = 120



class menu:
  def __init__(self, dimensions: tuple, pos: tuple, options: list, exitkey: int, title: str, visible: bool):
    self.dimensions = dimensions
    self.x = pos[0]
    self.y = pos[1]
    self.height = dimensions[0]
    self.width = dimensions[1]
    self.usewidth = dimensions[1] - 2
    self.visibility = visible
    self.options = options
    self.exit = exitkey
    self.title = title
    self.lines = [None] * (dimensions[0])
    self.dict = {'optionlist': options}

def genlines(q):
  q.options = q.dict['optionlist']
  q.lines[0] = '+' + '-' * q.usewidth + '+'
  x = 1
  for option in q.options:
    q.lines[x] = ('|' + 
                  option[0] + 
                  ' ' * (q.usewidth - len(option[0]) - len(str(option[1]))) + 
                  str(option[1]) + 
                  '|')
    if mod(q.usewidth, 2) == 0:
      q.lines[x + 1] = '|' + ' ' * round(((q.usewidth - 8 ) / 2)) + "Press '%c'" % (option[2]) + ' ' * (round(((q.usewidth - 8 ) / 2)) - 1) + '|'
    else:
      q.lines[x + 1] = '|' + ' ' * round(((q.usewidth - 9 ) / 2)) + "Press '%c'" % (option[2]) + ' ' * (round(((q.usewidth - 9 ) / 2))) + '|'
    x += 2
  while x < q.height:
    q.lines[x] = '|' + ' ' * q.usewidth + '|'
    x += 1
  q.lines[q.height - 1] = '+' + '-' * q.usewidth + '+'
    

a = menu(dimensionss, poss, optionss, exitkey, 'store', True)

genlines(a)

x = 0
for line in a.lines:
  stdscr.addstr(x, 1, line)
  x += 1
stdscr.refresh()
a.options[0][1] = 30

sleep(2)
genlines(a)

x = 0
for line in a.lines:
  stdscr.addstr(x, 1, line)
  x += 1
stdscr.refresh()