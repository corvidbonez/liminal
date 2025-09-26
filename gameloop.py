import os
import csv
import liminal.games as games
from liminal.tokens import Game_Tokens
import spotipy


desc_narration = []
vera_dialogue = []
claire_dialogue = []
cecil_dialogue = []
hugh_dialogue = []

MAG = "\033[38;5;197m"
REG = "\033[38;5;232m"
#claire csv import
with open('claire.csv', 'r') as claire_script:
  legible_claire = csv.reader(claire_script)
  for row in legible_claire:
    claire_dialogue.append(row[0])
#cecil csv import
with open('cecil.csv','r') as cecil_script:
  legible_cecil = csv.reader(cecil_script)
  for row in legible_cecil:
    cecil_dialogue.append(row[0])
#hugh csv import
with open('hugh.csv', 'r') as hugh_script:
  legible_hugh = csv.reader(hugh_script)
  for row in legible_hugh:
    hugh_dialogue.append(row[0])
#vera csv import
with open('vera.csv','r') as vera_script:
  legible_vera = csv.reader(vera_script)
  for row in legible_vera:
    vera_dialogue.append(row[0])
#descriptions csv import
with open('descriptions.csv', 'r') as desc_script:
  legible_desc = csv.reader(desc_script)
  for row in legible_desc:
   desc_narration.append(row[0])

Cecil = Game_Tokens("Copper", 1, "Cecil"),
Claire = Game_Tokens("Bronze", 5, "Claire"),
Hugh = Game_Tokens("Silver", 5, "Hugh"),
Vera = Game_Tokens("Gold", 10, "Vera")
token1 = "Cecil's Token"
token2 = "Claire's Token"
# token3 = "Hugh's Token"
token3 = "Vera's Token"
    ######################################################
#images
lvl1_image = "level1.png"
#display starting menu
def prompt():
  print("Welcome to Spaces! ^-^\n\nFufill all your duties as a janitor on each floor. You'll need tokens to progress. \n\n"+ "\033[1m"+ "\tHint: For extra 'uncanny-ness' throw on our playlist: [enter link here]"+"\033[0m"+"\n\nMoves: n for north e for east w for west and s for south.")

  input("Press 'Enter' to continue >> ")
BOLD = "\033[1m"
NON = "\033[0m"
#clears screen differently based on type of computer
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

#map dictionary
levels = {
  'Level1': {'North': 'Hallway', 'South':'Elevator', 'West': 'Classroom 305', 'East': 'Classroom 307', 'Games':['Hide and Seek','RPS'],'Token1':['bronze','copper']},
  'Level2': {'North': 'Stairs_2', 'South': 'Stairs_1', 'Games': ['21 Card', 'RPS Snake'],'Tokens':['silver','gold']}
}

#inventory
inventory = []
#janitors closet lvl 1
crate = ["12 AA batteries", "a flashlight", "a headlamp", "a power cord", "Windex™", "Clorox™", "and various rags"]
crate2 = ["Smelleze® Odor Remover","a mop", "an oats and honey granola bar", "an mp3 player", "glass cleaner"]



#stores player's current pos
location = ""
floor = "Level 1"
#gameloop cond.
floor_1 = True
floor_2 = False


clear()
prompt()

# function for first janitors closet
def janitorlvl1():
  clear()
  location = "Lvl 1 Janitor's Closet"
  j1 = 1
  print(f"You're in the {BOLD+location}{NON} \n")
  print(desc_narration[27])
  print(desc_narration[7])
  while j1 < 8:
    print(desc_narration[8]+BOLD)
    print(*crate, sep = ", ")
    print(NON+f"Inventory:{inventory}")
    jc1 = input(f"{BOLD}What would you like to pick up? {NON}(if you would like to exit, please 'exit')").lower()
    if jc1 == "batteries" or jc1 == "aa batteries":
      crate.remove("12 AA batteries")
      inventory.append("batteries(AA)")
      print(f"\n{'-'*27}")
      j1 += 1
    elif jc1 == "flashlight":
      crate.remove("a flashlight")
      inventory.append("flashlight")
      print(f"\n{'-'*27}")
      j1 += 1
    elif jc1 == "headlamp":
      crate.remove("a headlamp")
      inventory.append("headlamp")
      print(f"\n{'-'*27}")
      j1 += 1
    elif jc1 == "power cord" or jc1 == "cord":
      print("You pick it up and notice the wire is frayed. Oh well, that was useless wasn't it?")
    elif jc1 == "windex":
      crate.remove("Windex™")
      inventory.append("Windex™")
      print(f"\n{'-'*27}")
      j1 += 1
    elif jc1 == "clorox":
      crate.remove("Clorox™")
      inventory.append("Clorox™")
      print(f"\n{'-'*27}")
      j1 += 1
    elif jc1 == 'rags':
      crate.remove("and various rags")
      inventory.append("Rags")
      print(f"\n{'-'*27}")
    elif jc1 == "exit":
      j1 = 10
    else:
      print("You try, but it won't budge.")
  print(f"You leave the {BOLD+location}{NON}.\n")
  return True

#func for jan. lvl2
def janitorlvl2():
  location = "Lvl 2 Janitor's Closet"
  j1 = 1
  print(f"You're in the {BOLD+location}{NON}.")
  print(desc_narration[7])
  while j1 < 6:
    print(desc_narration[8]+BOLD)
    print(*crate2, sep = ", ")
    print(NON+f"Inventory:{inventory}")
    jc1 = input(f"{BOLD}What would you like to pick up? {NON}(if you would like to exit, please 'exit')").lower()
    if jc1 == "smelleze":
      crate2.remove("Smelleze® Odor Remover")
      inventory.append("Smelleze®)")
      print(f"\n{'-'*27}")
      j1 += 1
    elif jc1 == "mop":
      crate2.remove("a mop")
      inventory.append("mop")
      print(f"\n{'-'*27}")
      j1 += 1
    elif jc1 == "granola" or jc1 == "bar":
      crate2.remove("an oats and honey granola bar")
      inventory.append("granola bar")
      print(f"\n{'-'*27}")
      j1 += 1
    elif jc1[0:2] == "mp3":
      crate2.remove("an mp3 player")
      inventory.append("mp3 player")
      print(f"\n{'-'*27}")
      j1 += 1
    elif jc1[0:4] == "glass":
      crate2.remove("glass cleaner")
      inventory.append("glass cleaner")
      print(f"\n{'-'*27}")
      j1 += 1
    elif jc1 == "exit":
      j1 = 10
    else:
      print("You try, but it won't budge.")
  print(f"You leave the {BOLD+location}{NON}.\n")
  return False
  







  
#203 func --> 21 card & Hugh
def class203():
  location = "Classroom 203"
  print(f"You're in {BOLD+location}{NON}.")
  BLU = "\033[38;5;117m"
  print(BLU + f"{hugh_dialogue[0]}\n")
  print(BLU + f"{hugh_dialogue[1]}\n")
  print(BLU + f"{hugh_dialogue[2]}\n")
  print(BLU + f"{hugh_dialogue[3]}\n")
  input(NON+"Press 'Enter' to continue >>")
  games.start21()
  # inventory.append(token3)
  # Hugh[0].token_desc()
  # Hugh[0].token_face()
  

      
#305 func --> Hide n Seek & Cecil
def class305():
  GRN = "\033[38;5;34m"
  location = "Classroom 305"
  if token1 not in inventory:
    print(f"\n{'-'*27}")
    print(f"You're in {BOLD+location}{NON}.")
    print(f"{desc_narration[26]}\n")
    print(GRN+f"{cecil_dialogue[0]}\n")
    print(GRN+f"{cecil_dialogue[1]}\n")
    w = games.starths()
    if w:
      #u win dialogue and says smth important [probaly]
      print(NON+f"{cecil_dialogue[11]}\n")
      print(GRN+f"{cecil_dialogue[12]}\n"+NON)
      print(f"{cecil_dialogue[13]}\n")
      inventory.append(token1)
      Cecil[0].token_desc()
      Cecil[0].token_face()
    else:
      #u lose
      #clear()
      print("You wake up in the hallway dazed and confused.. what happened?")
      input("Press 'Enter' to continue >>")
      location = "hallway"
  else:
    print(f"You walk into {location}. It's been cleaned and no one's in there.")
  
  
#307 func
def class307():
  location = "Classroom 307"
  print(f"\n{'-'*27}")
  print(f"{desc_narration[10]}\n")
  if token2 not in inventory:
    print(f"Welcome to {location}!")
    print(f"{MAG + claire_dialogue[0]}\n")
    print(f"{REG + claire_dialogue[1]}\n")
    print(f"{REG + claire_dialogue[2]}\n")
    print(f"{MAG + claire_dialogue[3]}\n")
    print(f"{MAG + claire_dialogue[4]}\n")
    r = str(games.startRPS())
    if r == "win":
      print(f"{MAG + claire_dialogue[16]}\n")
      p = str(games.startRPS())
    elif r == "lose":
      print(f"{MAG + claire_dialogue[17]}\n")
      p = str(games.startRPS())
    else:
      print(f"{MAG + claire_dialogue[18]}\n")
      p = str(games.startRPS())
    print(f"{MAG + claire_dialogue[19]}\n")
    s = str(games.startRPS())
    print(f"{REG + claire_dialogue[20]}\n")
    input("Press 'Enter' to continue >>")
    clear()
    print(f"{MAG + claire_dialogue[21]}\n")
    inventory.append(token2)
    
    Claire[0].token_desc()
    Claire[0].token_face()
  else:
    print(f"You walk into {location}. It's been cleaned and no one's in there.")



#201 func vera 
def class201():
  PURP = "\033[38;5;91m"
  REG = "\033[38;5;232m"
  print(REG+f"{desc_narration[25]}\n")
  print(PURP+f"{vera_dialogue[0]}\n")
  print(PURP+f"{vera_dialogue[1]}\n")
  print(REG+f"{vera_dialogue[2]}\n")
  print(PURP+f"{vera_dialogue[3]}\n")
  print(PURP+f"{vera_dialogue[4]}\n")
  print(PURP+f"{vera_dialogue[5]}\n")
  print(PURP+f"{vera_dialogue[6]}\n")
  input(REG +"Press 'Enter' to continue >>")
  clear()
  games.dgOppWins()
  print(PURP +f"{vera_dialogue[7]}\n")
  input("Try again?")
  clear()
  games.dgOppWins()
  print(REG +f"{vera_dialogue[8]}\n")
  print(REG +f"{vera_dialogue[9]}\n")
  print(PURP +f"{vera_dialogue[10]}\n")
  print(REG +f"{vera_dialogue[11]}\n")
  print(PURP +f"{vera_dialogue[12]}\n")
  print(REG +f"{vera_dialogue[13]}\n")
  print(PURP +f"{vera_dialogue[14]}\n")
  print(REG +f"{desc_narration[20]}\n")
  print(PURP +f"{vera_dialogue[15]}\n")
  print(REG +f"{desc_narration[21]}\n")
  inventory.append(token3)
  Vera.token_desc()
  Vera.token_face()

#tokens 2 for now depends on game wins and stuff
def stairslvl1():
  if token1 in inventory and token2 in inventory:
    return True
#token 3 for level 2
def stairslvl2():
  if token3 in inventory:
    return True
#BRUH 


#level 1 loop :)
def Level1():
  clear()
  jreturn = False
  #display info to player
  print(desc_narration[0])
  print(f"Welcome to {BOLD+floor}!\n{NON+'-'*27}")

  #print desc.
  print(f"{desc_narration[1]}\n")
  print(f"{desc_narration[2]}\n")
  print(f"{desc_narration[3]}\n")
  print(f"{desc_narration[4]}\n{'-'*27}")

  input("Press 'Enter' to continue >> ")
  clear()
  
  while True:
    #loop for directions
    f1 = input(f"Choose a direction: North, South, East, West\nInventory:{inventory}\n \t>>")
    clear()
    if f1.lower()[0:1] == "s":
      print(f"{desc_narration[5]}\n")
    elif f1.lower()[0:1] == "e":
      if not jreturn:
        print("\nMaybe I should pick up some supplies at the Janitor's Closet first..\n")
      else:
        clear()
        class305()
    elif f1.lower()[0:1] == "w":
      clear()
      jreturn = janitorlvl1()
      location = "hallway"
      break
    elif f1.lower()[0:1] == "n":
      location = "hallway"
      print(f"\nYou move north towards the {BOLD+location}{NON}.")
      print(f"{desc_narration[9]}\n")
      break
  while location == "hallway":
    f1 = input(f"Choose a direction: North, South, East, West\nInventory: {inventory}\n \t>>")
    clear()
    if f1.lower()[0:1] == "s":
      print(f"{desc_narration[11]}\n")
    elif f1.lower()[0:1] == "n":
      if stairslvl1():
        clear()
        print(f"{desc_narration[12]}\n")
        return False
      else:
        print(f"{desc_narration[13]}\n")
    elif f1.lower()[0:1] == "e":
      if not jreturn:
        print("\nMaybe I should pick up some supplies at the Janitor's Closet first..\n")
      else:
        clear()
        class305()
    elif f1.lower()[0:1] == "w":
        print(desc_narration[23])
        whichw = input("Where would you like to go >>").lower()
        if whichw[0] == "j" or whichw[0:5]=="closet":
          clear()
          jreturn = janitorlvl1()
          location = "hallway"
        elif (whichw[0] == "r" or whichw[0:4]=="class") and not jreturn:
          print("\nMaybe I should pick up some supplies at the Janitor's Closet first..\n")
        else:
          clear()
          class307()
    else:
      print("Sorry, you can't go that way.")


def strt():
  Level1()
  if not Level1():
    Level2()


#########################################level 2 yaY
def Level2():
  #os.remove(lvl1_image)
  clear()
  floor_2 = True
  #print end msg for lvl 1
  print(f"{desc_narration[17]}\n")
  input("Press enter to continue>> ")
  clear()
  print(f"{desc_narration[14]}\n")
  print(f"{desc_narration[15]}\n")
  

  #display info to player
  floor = "Level 2"
  print(desc_narration[16])
  print(f"Welcome to {floor}!\n{'-'*27}")


  input("Press 'Enter' to continue >>")
  clear()

  #start while loop for lvl 2
  while floor_2:
    f2 = input(f"You know the drill. Inventory:{inventory}\nChoose a direction >> ").lower()
    clear()
    if f2.lower()[0:1] == "s":
      print(f"{desc_narration[11]}\n")
    elif f2.lower()[0:1] == "e":
      clear()
      print(f"\n{'-'*27}")
      #class201()
      print("It's too dark. I shouldn't go that way..")
    elif f2.lower()[0:1] == "w":
      clear()
      print(f"{desc_narration[18]}\n")
      print(desc_narration[19])
      f3 = input("Which one? >>").lower()
      if f3.lower()[0:4] == "class" or f3.lower()[0:1] == "r":
        class203()
      elif f3.lower()[0:1] == "j" or f3.lower()[0:5] == "closet":
          janitorlvl2()
    elif f2.lower()[0:1] == "n":
      if stairslvl2():
        #GAME OVER
        clear()
        print(f"{desc_narration[20]}\n")
        print(games.PURP+f"{vera_dialogue[15]}\n"+NON)
        print(f"{vera_dialogue[16]}\n")
        input("Press 'Enter' to continue >>")
        clear()
        print(BOLD+f"{vera_dialogue[17]}\n")
        print(BOLD+f"{vera_dialogue[18]}\n")
        return False
      else:
        print(f"{desc_narration[24]}\n")
    else:
      print("Sorry, you can't go that way.")