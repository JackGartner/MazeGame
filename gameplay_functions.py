################## imports
import display_functions
from getkey import getkey, keys
import emoji 
import time
import random


################## constants

TITLE = "Cheese Maze"
DEVELOPER = "Jack Gartner"
HISTORY = "A mouse wants eat his cheese, Make it to the Hashtag to win, watch out for plus signs!"
INSTRUCTIONS = "left arrow key\t\t\tto move left\nright arrow key\t\t\tto move right\nup arrow key\t\t\tto move up\ndown arrow key\t\t\tto move down\npress q\t\t\t\t\tto quit"

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"

RED_B = "\033[41m"
GREEN_B = "\033[42m"
YELLOW_B = "\033[43m"
BLUE_B = "\033[44m"
PURPLE_B = "\033[45m"
CYAN_B = "\033[46m"
WHITE_B = "\033[47m"
BLACK_B = "\033[49m"

WHITE_ON_BLACK = WHITE + BLACK_B
BLACK_ON_WHITE = BLACK + WHITE_B
WHITE_ON_BLUE = WHITE + BLUE_B

RESET_COLORS = "\033[0m"

################## variables


theme = WHITE_ON_BLACK

player = emoji.emojize(":mouse:")
player2 = emoji.emojize(":mouse:")
#player = RED + "M" + theme
#player = CYAN_B + " " + theme
#player = WHITE_ON_BLUE + "M" + theme

# initial position of player
playerRow = 14
playerCol = 11
player2Row = 12
player2Col = 2
playerMove = "d"
player2Move = "d"
rightEdge = 15
leftEdge = 1

# item data
itemRow = 0
itemCol = 0
itemActive = True # item flag in play or not

################## functions

def setup():
  print(theme, end="")
  # hide cursor (use h instead of l to show cursor)
  print("\033[?25l", end="")  
  # clear screen and set cursor to top left corner
  print("\033[2J", end="") 

def refreshDisplay():

  player2 = emoji.emojize(":mouse:")
  player2Row = 12
  player2Col = 2 
  player2Move = "d"


  print(theme, end="")
  # clear screen and set cursor to top left corner
  print("\033[2J", end="")
  print("\033[0;0H", end="")

  display_functions.displayTitle()
  display_functions.displayBoard()

  # display player 
  print("\033[" + str(50) + ";" + str(50) + "H", end="")
  print(player) 

  print("\033[" + str(12) + ";" + str(2) + "H", end="")
  print(player2) 
  
  while player2Move != "q":
   player2Move = getkey()

   # clear player
   print("\033[" + str(player2Row) + ";" + str(player2Col) + "H", end="")
   print(" ", end = "")

   if player2Move == "q":
     break
   elif player2Move == "a":
     player2Col -= 1
   elif player2Move == keys.LEFT:
     player2Col -= 1
   elif player2Move == "d":
     player2Col += 1
   elif player2Move == keys.RIGHT:
     player2Col += 1
   elif player2Move == keys.DOWN:
     player2Row += 1
   elif player2Move == keys.UP:
     player2Row -= 1
   elif player2Move == "c":
     player2 = emoji.emojize(":cat:")
   else: 
     print("invalid input")

   # display player in new position
   print("\033[" + str(player2Row) + ";" + str(player2Col) + "H", end="")
   print(player2)

   # top and bottom wall
   if player2Row > 18 or player2Row < 13:
     break
   # left and right wall
   if player2Col < 1  or player2Col > 15:
     break
   # 5, 13 spike
   if player2Col == 5 and player2Row == 13:
     break
   # 5, 15 spikes
   if player2Col <= 5 and player2Row == 15:
     break
   # 9, 17 spike
   if player2Col == 9 and player2Row <= 17:
     break
   # 3-8, 317
   if player2Col >= 3 and player2Col <= 8 and player2Row == 17 :
     break
   # 10-14, 15
   if player2Col >= 10 and player2Col <= 14 and player2Row == 15:
     break
   # 12-16, 17
   if player2Col >= 12 and player2Col <= 16 and player2Row == 17 :
     break

   # win tile
   if player2Col == 2 and player2Row == 13:
     print("\n\n\n\n\n\nwinner!")
     time.sleep(0.5)
     break
