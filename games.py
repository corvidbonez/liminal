import random
import csv
from random import randrange
import liminal.gameloop as gameloop

#lists to store csv
vera_dialogue = []
claire_dialogue = []
cecil_dialogue = []
hugh_dialogue = []
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


#############################################################
MAG = "\033[38;5;197m"
REG = "\033[38;5;232m"

def rps(): 
  rps = ["rock", "paper", "scissors"]
  userPick = input(REG + claire_dialogue[6])
  oppPick = rps[random.randint(0,2)]
  print(MAG + claire_dialogue[7])
  cho = print(f"\033[38;5;232mYou chose {userPick}\nClaire chose {oppPick}")

  if userPick.lower()[0:1] == "r":
    userPick = rps[0]
    if oppPick == rps[1]:
      print(MAG + claire_dialogue[8])
      print(REG + claire_dialogue[11])
      return "lose"
    if oppPick == rps[2]:
      print(REG + claire_dialogue[10])
      print(MAG + claire_dialogue[9])
      return "wins"
    if oppPick == rps[0]:
      k = random.randint(1,2)
      if k == 1:
        print(MAG + claire_dialogue[12])
        return "tie"
      else:
        print(REG + claire_dialogue[13])
        return "tie"
  elif userPick.lower()[0:1] == "p":
    userPick = rps[1]
    cho
    if oppPick == rps[2]:
      print(MAG + claire_dialogue[8])
      print(REG + claire_dialogue[11])
      return "lose"
    if oppPick == rps[0]:
      print(REG + claire_dialogue[10])
      print(MAG + claire_dialogue[9])
      return "wins"
    if oppPick == rps[1]:
      k = random.randint(1,2)
      if k == 1:
        print(MAG + claire_dialogue[12])
        return "tie"
      else:
        print(REG + claire_dialogue[13])
        return "tie"
  elif userPick.lower()[0:1] == "s":
    userPick = rps[2]
    cho
    if oppPick == rps[0]:
      print(MAG + claire_dialogue[8])
      print(REG + claire_dialogue[11])
      return "lose"
    if oppPick == rps[1]:
      print(REG + claire_dialogue[10])
      print(MAG + claire_dialogue[9])
      return "wins"
    if oppPick == rps[2]:
      k = random.randint(1,2)
      if k == 1:
        print(MAG + claire_dialogue[12])
        return "tie"
      else:
        print(REG + claire_dialogue[13])
        return "tie"
  else:
    print("invalid")
    rpsPlay = False

def startRPS():
  play = input(MAG + f"{claire_dialogue[5]} (y/n):\n")
  if play.lower()[0:1] == "y":
    rpsPlay = True
    if rpsPlay:
      rps() 
  elif play.lower()[0:1] == "n":
    print(MAG + claire_dialogue[22] + REG)
    gameloop.location = "hallway"
#startRPS()
###############################################################
#can un change the name of ur color to wtv the color is thx
BLU = "\033[38;5;117m"
#21
def cg21Deck():
  heart =[]
  diamond= []
  spade = []
  club = []
  for hearts in range(2, 11):
    heart.append(str(hearts) + "♥️")
  heart.append("Ace♥️")
  heart.append("Jack♥️")
  heart.append("Queen♥️")
  heart.append("King♥️")
  for dmds in range(2, 11):
    diamond.append(str(dmds) + "◆︎")
  diamond.append("Ace◆︎")
  diamond.append("Jack◆︎")
  diamond.append("Queen◆︎")
  diamond.append("King◆︎")
  for spd in range(2, 11):
    spade.append(str(spd)+ "♠️")
  spade.append("Ace♠️")
  spade.append("Jack♠️")
  spade.append("Queen♠️")
  spade.append("King♠️")
  for clubs in range(2, 11):
    club.append(str(clubs)+ "♣️")
  club.append("Ace♣️")
  club.append("Jack♣️")
  club.append("Queen♣️")
  club.append("King♣️")
  deck = [heart, diamond, spade, club]
  randSuit = deck[random.randint(0, 3)]
  randCard = randSuit[random.randint(0, 12)]
  return randCard

def yourvalues():
  value = 0
  userCard1 = cg21Deck()
  userCard2 = cg21Deck()
  print(REG+f"Your first card is {userCard1}.\nYour second card is {userCard2}")
  #card1
  if userCard1[0:1] == "K" or userCard1[0:1] == "Q" or userCard1[0:1] == "J":
    value += 10
  if userCard1[0:1] == "A":
    ace = input(REG+"You got an Ace Card. Do you want it to be worth 1 or 11 points:")
    if ace == "1":
      value += 1
    else:
      value += 11
  if userCard1[0:1] == "2" or userCard1[0:1] == "3" or userCard1[0:1] == "4" or userCard1[0:1] == "5" or userCard1[0:1] == "6" or userCard1[0:1] == "7" or userCard1[0:1] == "8" or userCard1[0:1] == "9" or userCard1[0:2] == "10":
    for i in range(2, 10):
      if userCard1[0:1] == str(i):
        value += i
  if userCard1[0:2] == "10":
    value += 10
  #card2
  if userCard2[0:1] == "K" or userCard2[0] == "Q" or userCard2[0] == "J":
    value += 10
  if userCard2[0:1] == "A":
    ace2 = input(REG+"You got an Ace Card. Do you want it to be worth 1 or 11 points:")
    if ace2 == "1":
      value += 1
    else:
      value += 11
  if userCard2[0:1] == "2" or userCard2[0:1] == "3" or userCard2[0:1] == "4" or userCard2[0:1] == "5" or userCard2[0:1] == "6" or userCard2[0:1] == "7" or userCard2[0:1] == "8" or userCard2[0:1] == "9" or userCard2[0:2] == "10":
    for i in range(2, 10):
      if userCard2[0:1] == str(i):
        value += i
  if userCard2[0:2] == "10":
    value += 10
  return value


def oppvalue():
  value = 0
  userCard1 = cg21Deck()
  userCard2 = cg21Deck()
  #card1
  if userCard1[0] == "K" or userCard1[0] == "Q" or userCard1[0] == "J":
    value += 10
  if userCard1[0:1] == "A":
    ace = random.randint(1, 2)
    if ace == 1:
      value += 1
    else:
      value += 11
  if userCard1[0:1] == "2" or userCard1[0:1] == "3" or userCard1[0:1] == "4" or userCard1[0:1] == "5" or userCard1[0:1] == "6" or userCard1[0:1] == "7" or userCard1[0:1] == "8" or userCard1[0:1] == "9" or userCard1[0:2] == "10":
    for i in range(2, 10):
      if userCard1[0:1] == str(i):
        value += i
  if userCard1[0:2] == "10":
    value += 10
  #card2
  if userCard2[0] == "K" or userCard2[0] == "Q" or userCard2[0] == "J":
    value += 10
  if userCard2[0:1] == "A":
    ace2 = ace = random.randint(1, 2)
    if ace2 == "1":
      value += 1
    else:
      value += 11
  if userCard2[0:1] == "2" or userCard2[0:1] == "3" or userCard2[0:1] == "4" or userCard2[0:1] == "5" or userCard2[0:1] == "6" or userCard2[0:1] == "7" or userCard2[0:1] == "8" or userCard2[0:1] == "9" or userCard2[0:2] == "10":
    for i in range(2, 10):
      if userCard2[0:1] == str(i):
        value += i
  if userCard2[0:2] == "10":
    value += 10
  return value


def hit(val):
  newCard = cg21Deck()
  if newCard[0] == "K" or newCard[0] == "Q" or newCard[0] == "J":
    val += 10
  if newCard[0:1] == "A":
    ace = input("You got an Ace Card. Do you want it to be worth 1 or 11 points:")
    if ace == "1":
      val += 1
    else:
      val += 11
  if newCard[0:1] == "2" or newCard[0:1] == "3" or newCard[0:1] == "4" or newCard[0:1] == "5" or newCard[0:1] == "6" or newCard[0:1] == "7" or newCard[0:1] == "8" or newCard[0:1] == "9" or newCard[0:2] == "10":
    for i in range(2, 10):
      if newCard[0:1] == str(i):
        val += i
  if newCard[0:2] == "10":
    val += 10
  return newCard, val

def oppHit(val):
  newCard = cg21Deck()
  if newCard[0] == "K" or newCard[0:5] == "Q" or newCard[0:5] == "J":
    val += 10
  if newCard[0:1] == "A":
    ace = random.randint(1, 2)
    if ace == 1:
      val += 1
    else:
      val += 11
  if newCard[0:1] == "2" or newCard[0:1] == "3" or newCard[0:1] == "4" or newCard[0:1] == "5" or newCard[0:1] == "6" or newCard[0:1] == "7" or newCard[0:1] == "8" or newCard[0:1] == "9" or newCard[0:2] == "10":
    for i in range(2, 10):
      if newCard[0:1] == str(i):
        val += i
  if newCard[0:2] == "10":
    val += 10
  return newCard, val


def cg21():
  
  #print(hugh_dialogue)
  uvalue = yourvalues()
  oppvalues = oppvalue()
  print(REG+f"Your value is {uvalue}.")
  for i in range(10):
    hors = input(REG+"Do you want to hit or stay: ")
    if hors.lower() == "hit":
      nc, nv = hit(uvalue)
      print(REG+f"Your new card is {nc}")
      print(REG+f"Your new value is {nv}")
      uvalue = nv
      if uvalue > 21:
        print(REG+"You busted. Your turn is over..")
        break
    else: 
      print(REG+"You decide to stay.")
      break
  print(REG+"Your turn is over.")
  for i in range(10):
    oppnc, oppnv = oppHit(oppvalues)
    #print(oppvalues)
    if oppvalues < 17:
      print(BLU+"Hugh chooses to hit.")
      oppvalues = oppnv
      #print(oppvalues)
      perc = random.randint(1,2)
      if perc ==2 and oppvalues<19:
        print(BLU+"Hugh chooses to stay")
        break
    else:
      print(BLU+"Hugh chooses to stay.")
      break

  print(REG+"You both place your cards faceup.")
  print(REG+f"Your final value was {uvalue}. Hugh's was {oppvalues}.")
  if uvalue>21 and oppvalues>21:
    print("You both busted. It's a draw.")
    print(BLU + hugh_dialogue[7]+REG)
  elif uvalue>21 and oppvalues<21:
    print("You busted and Hugh's value was under 21. Hugh wins.")
    print(BLU + hugh_dialogue[9])
    print(hugh_dialogue[11]+REG)
  elif uvalue>21 and oppvalues==21:
    print("You busted and Hugh got 21. You lose.")
    print(BLU + hugh_dialogue[9])
    print(hugh_dialogue[11]+REG)
  elif uvalue<21 and oppvalues==21:
    print("You got under 21 and Hugh got 21. You lose.")
    print(BLU + hugh_dialogue[9])
    print(hugh_dialogue[11]+REG)
  elif uvalue==21 and oppvalues==21:
    print("You both got 21. It's a draw.")
    print(BLU + hugh_dialogue[7])
    print(hugh_dialogue[10])
    print(hugh_dialogue[6]+REG)
  elif uvalue<21 and oppvalues<21:
    if uvalue > oppvalues:
      print("You both got under 21 but your score was higher. You win!")
      print(BLU + hugh_dialogue[8])
      print(hugh_dialogue[10])
      print(hugh_dialogue[6]+REG)
      gameloop.class201()
    else:
      print("You both got under 21 but your score was lower. You lose.")
      print(BLU + hugh_dialogue[9])
      print(hugh_dialogue[11]+REG)
  elif uvalue<21 and oppvalues >21:
    print("Hugh busted. You win!")
    print(BLU + hugh_dialogue[8])
    print(hugh_dialogue[10])
    print(hugh_dialogue[6]+REG)
    gameloop.class201()
  elif uvalue==21 and oppvalues != 21:
    print("You got 21. You win!")
    print(BLU + hugh_dialogue[8])
    print(hugh_dialogue[10])
    print(hugh_dialogue[6]+REG)
    gameloop.class201()
  elif uvalue != 21 and oppvalue == 21:
    print("Hugh got 21. You lose.")
    print(BLU + hugh_dialogue[9])
    print(hugh_dialogue[11]+REG)

def start21():
  play = input(BLU + f"{hugh_dialogue[4]} (y/n):\n")
  if play.lower()[0:1] == "y":
    bjPlay = True
    if bjPlay:
      cg21()
  elif play.lower()[0:1] == "n":
    print("Come on, it'll be fun!")
    cg21()
    
#start21() 
#########################################################################
PURP = "\033[38;5;91m"
NON = "\033[0m"
#dice game where opp always winss
def dgOppWins():
  print(REG+ "You roll the dice")
  d = random.randint(2,8)
  print(REG+ f"(You watch the dice stumble about)\nYou rolled a {d}")
  f = random.randint(9,12)
  print(PURP + "My turn..")
  print(REG+ f"You wait impatiently for the dice to steady itself...\nVera rolled a {f}")
#dgOppWins()
########################################
#hide and seek
GRN= "\033[38;5;34m"
BOLD = "\033[1m"
def hideandseek():
  places_to_hide = ['Behind a chair','Inside an emtied bookself ',"In the very corner of the room","Under the teacher's desk"]
  #gameloop.clear()
  print("You look around..\n"+BOLD)
  print(", ".join(places_to_hide) +"\n" + NON)
  user_input = (input("(Hmm where should I hide..) >>")).lower()
  print ("you choose to hide by the " + user_input)
  gameloop.clear()
  print( GRN +f"{cecil_dialogue[4]}\n"+NON)
  oppChoice =[]
  oppChoice.append("desk")
  oppChoice.append("chair")
  oppChoice.append("bookshelf")
  oppChoice.append("corner")
  oppc = oppChoice[random.randint(0,3)]
  userc = ""
  k = True
  while k:
    if user_input[0] == "d":
      userc = "desk"
      break
    elif user_input[0:2] == "ch":
      userc = "chair"
      break
    elif user_input[0:2] == "co":
      userc = "corner"
      break
    elif user_input[0] == "b":
      userc = "bookshelf"
      break
    else:
      print("You can't hide there..")
  print("Cecil looks around the "+ oppc+"...\n")
  oppChoice.remove(oppc)
  if userc != oppc:
    randomPrint = random.randint(1,3)
    if randomPrint == 1:
      print (GRN+f"\n{cecil_dialogue[5]}\n"+NON)
      oppc = oppChoice[random.randint(0,3)]
      print("Cecil looks around the "+ oppc+"...\n")
    elif randomPrint == 2:
      print (GRN+f"\n{cecil_dialogue[6]}\n"+NON)
      oppc = oppChoice[random.randint(0,3)]
      print("Cecil looks around the "+ oppc+"...\n")
    else:
      print (GRN+f"\n{cecil_dialogue[7]}\n"+NON)
      oppc = oppChoice[random.randint(0,2)]
      print("Cecil looks around the "+ oppc+"...\n")
  if userc == oppc:
    #you lose
    print(GRN+"Found You! >:)\n")
    print (GRN+f"\n{cecil_dialogue[8]}\n"+NON)
    return False
    #more dialogue don't replay
  else:
    #player win
    print (GRN+f"{cecil_dialogue[9]}\n")
    print (GRN+BOLD+f"{cecil_dialogue[10]}\n"+NON)
    #hideandseek()
    return True
    
#starts hide n seek
def starths():
  play = input(GRN+f"{cecil_dialogue[2]}\n")
  if play.lower()[0:1] == "y":
    hsplay = True
    if hsplay:
      print(GRN+f"{cecil_dialogue[3]}\n" +NON)
      w = hideandseek()
      return w
  elif play.lower()[0:1] == "n":
    print(GRN+"\nYou hide and I try to find you. That's all there is to it ...okay go hide now"+NON)
    w = hideandseek()
    return w
#starths()
