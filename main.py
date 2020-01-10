import curses
import winrglib


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

x = 1
y = 1
options = [['upgrade 1', 10, 490, 'get1'], 'upgrade 2', 'upgrade 3', 'prestige']
costs = [10,20,30,100]
outputs = ['get1', 'get2', 'get3' 'getp']
maxheight = 20
width = 20
exitkey = 120

usewidth = width - 2
x = 0
for option in options:
  x += 1
  thefrigginlengthofthelinesspaces = usewidth - len(option) - len(str(costs[x]))
  if thefrigginlengthofthelinesspaces >= 5:
    lines = [option + ' ' * thefrigginlengthofthelinesspaces + str(costs)]