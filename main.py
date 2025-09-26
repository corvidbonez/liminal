import liminal.gameloop as gameloop
import os
import liminal.games as games
import csv
import liminal.tokens as tokens

#csv lists
desc_narration = []
vera_dialogue = []
claire_dialogue = []
cecil_dialogue = []
hugh_dialogue = []

#CSV IMPORTS
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


#gameloop.strt()
gameloop.Level1()
gameloop.Level2()