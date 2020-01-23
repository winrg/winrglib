######################################################
#                                                    #
#            winrg function library 1.1.0            #
#                    Jan. 2020                       #
#             Do with this as you please             #
#                                                    #
######################################################

version = '1.0.1'

#define a curses message bubble
def bubble(screen, x, y, text):
  length = len(text)
  screen.addstr(y - 5, x, ' ' + '_' * length)
  screen.addstr(y - 4, x, '|' + ' ' * length + '|')
  screen.addstr(y - 3, x, '|' + text + '|')
  screen.addstr(y - 2, x, '| ' + '_' * (length - 1) + '|')
  screen.addstr(y - 1, x, '|/')