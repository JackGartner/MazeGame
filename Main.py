# Jack Gartner
# Works Cited
# https://www.webfx.com/tools/emoji-cheat-sheet

################## imports
import display_functions
import gameplay_functions
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

#theme = WHITE_ON_BLACK

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

boundaryDetection = True
internalDetection = True
doorLocked = True

################## functions

# found in respective files

################## main

gameplay_functions.setup()

# displayItem() (under construction)

display_functions.displayTitle()

display_functions.displayBoard()


# display player in original position
print("\033[" + str(playerRow) + ";" + str(playerCol) + "H", end="")
print(player)

# loop until player quits or hits a boundary
while playerMove != "q":
  playerMove = getkey()

  # clear player
  print("\033[" + str(playerRow) + ";" + str(playerCol) + "H", end="")
  print(" ", end = "")

  if playerMove == "q":
    break
  elif playerMove == "a":
    playerCol -= 1
  elif playerMove == keys.LEFT:
    playerCol -= 1
  elif playerMove == "d":
    playerCol += 1
  elif playerMove == keys.RIGHT:
    playerCol += 1
  elif playerMove == "s":
    playerRow += 1
  elif playerMove == keys.DOWN:
    playerRow += 1
  elif playerMove == "w":
    playerRow -= 1
  elif playerMove == keys.UP:
    playerRow -= 1
  elif playerMove == "c":
    player = emoji.emojize(":cat:")
  else: 
    print("invalid input")

  # display player in new position
  print("\033[" + str(playerRow) + ";" + str(playerCol) + "H", end="")
  print(player)



  if boundaryDetection == True:

    # top and bottom wall
   if playerRow > 18 or playerRow < 13:
     break
   # left and right wall
   if playerCol < 1  or playerCol > 15:
     break

   if internalDetection == True:
     # 5, 13 spike
     if playerCol == 5 and playerRow == 13:
       break
     # 5, 15 spikes
     if playerCol <= 5 and playerRow == 15:
       break
     # 9, 17 spike
     if playerCol == 9 and playerRow <= 17:
       break
     # 3-8, 317
     if playerCol >= 3 and playerCol <= 8 and playerRow == 17 :
       break
     # 10-14, 15
     if playerCol >= 10 and playerCol <= 14  and playerRow == 15:
       break
     # 12-16, 17
     if playerCol >= 12 and playerCol <= 16 and playerRow == 17 :
       break




  ##### Locked Door and Key

  if playerCol > 5 and playerCol < 8 and playerRow == 13 :
   print("\n\n\n\n\n\nKey Obtained ")
   doorLocked = False

  if doorLocked == True :

    if playerCol == 4 and playerRow == 14:
      print("\n\n\n\n\n\nYou must get the key in order to enter")
      break

  if playerCol == 3 and playerRow == 14:
    print("\n\n\n\n\n\n\nDoor Unlocked")




  ##### 16, 17 teleport 
  if (playerCol >= 13 and playerCol <= 16) and playerRow == 18 :
    print("\033[" + str(12) + ";" + str(2) + "H", end="")
    print(player2)
    print(" ", end = "")
    gameplay_functions.refreshDisplay()

  ##### Power Up

  if playerCol == 15 and playerRow == 13 :
    print("\n\n\n\n\n\nPower Up!")
    player = emoji.emojize(":cat:")
    internalDetection = False
    doorLocked = False
    
 
  
  
  # win tile
  if playerCol == 2 and playerRow == 14:
    print("\n\n\n\n\n\n\n\nwinner!")
    time.sleep(0.5)
    break



# position the red command line prompt far down the screen
print("\033[15;0H")
print("\n\n\n\n\n\n\n\ngoodbye")
