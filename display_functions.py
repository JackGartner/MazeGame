############# constants
TITLE = "Cheese Maze"
DEVELOPER = "Jack Gartner"
HISTORY = "A mouse wants eat his cheese, Make it to the Hashtag to win, watch out for plus signs, $ is a teleport, P is a power up, Obtain the Key (K) in order to unlock the door (D)"
INSTRUCTIONS = "left arrow key\t\t\tto move left\nright arrow key\t\t\tto move right\nup arrow key\t\t\tto move up\ndown arrow key\t\t\tto move down\npress q\t\t\t\t\tto quit"

############# functions

def displayTitle():
  print(TITLE)
  print("By " + DEVELOPER)
  print()
  print(HISTORY)
  print()
  print(INSTRUCTIONS)
  print()


def displayBoard():
  print("-----------------")
  print("|   +\033[36mK\033[37m  +      \033[33mP\033[37m|")
  print("|\033[32m#\033[37m  \033[31mD\033[37m   +       |")
  print("|++++   ++++++  |")
  print("|       +       |")
  print("|  ++++++  +++++|")
  print("|              \033[34m$\033[37m|")
  print("-----------------")

