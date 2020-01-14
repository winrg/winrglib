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
lines = [0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2, ]

x = 1
y = 1
options = [['upgrade 1', '10', 490, 'get1'], ['upgrade 2', '20', 500, 'get2'], ['upgrade 3', '30', 510, 'get3'], ['prestige', '100', 80, 'getp']]
height = 20
width = 20
exitkey = 120

usewidth = width - 2
x = 0
for option in options:
  thefrigginlengthofthelinesspaces = usewidth - len(option[1]) - len(option[0])
  if thefrigginlengthofthelinesspaces >= 5:
    lines[x] = '|' + option[0] + ' ' * thefrigginlengthofthelinesspaces + option[1] + '|'
stdscr.addstr(1, 1, '+' + '-' * usewidth + '+')
stdscr.addstr(2, 1, lines[0])
stdscr.refresh()