from fpdf import FPDF
import os.path
from os import path
import json

#pre-startup
input("Welcome to Pathfinder creature maker! Press Enter once you have entered all your desired values into the 'input.JSON' file\n")

#vars
pdf = FPDF('P', 'mm', 'letter')
#region
f = open("input.JSON", 'r')
myJson = f.read()
f.close()

#convert json to python dict so that the program can read it.
myJson = json.loads(myJson)

#start adding json values to python variables
desc = myJson["description"]

name = myJson["name"]
traits = myJson["traits"]

perception = myJson["perception"]
senses = myJson["senses"]

skills = myJson["skills"]

abNames = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
abScrs = myJson["abilityScores"]

ac = myJson["ac"]

throws = myJson["throws"]

hp = myJson["hp"]

speed = myJson["speed"]

attacks = myJson["attacks"]

spells = myJson["spells"]

inventory = myJson["inventory"]

ps = myJson["ps"]

myDir = myJson["saveDirectory"]
#endregion


#funcs
def convert(string):
    li = list(string.split(', '))
    return li

def convert2(string):
    li = list(string.split('\n\n'))
    return li

def doPdf():
    pdf.add_page()

    pdf.set_auto_page_break(True, 1)

    # Set font
    pdf.set_font('Times', 'B', 36)
    # Move to 8 cm to the right
    pdf.cell(80)
    # Centered text in a framed 20*10 mm cell and line break
    pdf.cell(20, 10, 'Pathfinder NPC Maker', 0, 1, 'C')
    #vertical line
    pdf.cell(80)
    pdf.cell(20, 10, '-------------------------------------', 0, 1, 'C')

    
    #line break
    pdf.multi_cell(w=20, h=10, txt="\n\n", ln=1)


    #description
    
    #font size
    pdf.set_font_size(12)

    #print a description if one exists
    if (desc != ''):
        pdf.multi_cell(0, 5, desc+'\n\n', ln=1)

    #big font size
    pdf.set_font_size(26)

    #name
    pdf.cell(200, 10, name, 1, 1)

    #small font size
    pdf.set_font_size(12)

    #traits
    for i in range(len(traits)):
        pdf.cell(25, 10, traits[i], 1, 0)
    
    #line break
    pdf.multi_cell(w=20, h=10, txt="\n", ln=1)

    #stats
    pdf.multi_cell(0, 10, "Perception "+perception+'; '+senses, ln=1)
    pdf.multi_cell(0, 10, "Skills: "+skills, ln=1)

    for i in range(6):
        x = 0
        endsplit = ", "
        #add comma to the end unless it's the last one
        if i == 5:
            x = 1
            endsplit = ''
        #print the line
        pdf.cell(20, 10, str(abNames[i])+' '+str(abScrs[i])+endsplit, ln=x)

    #vertical line
    pdf.cell(10, 10, '-'*100, ln=1)
    pdf.cell(10, 10, "AC: "+ac+'; Fort '+throws[0]+', Ref '+throws[1]+', Will '+throws[2], ln=1)
    pdf.cell(10, 10, "HP "+hp, ln=1)
    #vertical line
    pdf.cell(10, 10, '-'*100, ln=1)
    pdf.cell(10, 10, "Speed: "+speed, ln=1)
    #print the attacks (can print as many as you want)
    for i in range(len(attacks)):
        pdf.multi_cell(0, 5, '\n'+attacks[i], ln=1)
    #vertical line
    pdf.cell(10, 10, '-'*100, ln=1)
    #spells
    if (spells != ''):
        pdf.multi_cell(0, 5, 'spells: '+spells+'\n\n', ln=1)
    #inventory
    if (inventory != ''):
        pdf.multi_cell(0, 5, 'inventory: '+inventory+'\n\n', ln=1)
    #post scriptum
    if (ps != ''):
        pdf.multi_cell(0, 5, ps, ln=1)


#program

#depricated
#region
"""
name = input("What would you like to name your Creature?\n")

desc = input("\n\nEnter a description for your creature (this is displayed above the creature name)\n")

traits = convert(input("\n\nWhat traits does your creature have? Please seperate each item by a space and comma.\n"))

perception = input("\n\nPerception? Be sure to add the '+' or '-'.\n")
senses = input("\n\nenter the senses\n")

skills = input("\n\nenter your creature's skills.\n")

print("\n\nenter your ability score bonuses (ex: +3). Be sure to include the '+' or '-':\n\n")
for i in range(len(abNames)):
    abScrs.append(input(abNames[i]+' '))

ac = input("\n\nenter creature AC.\n")

print("\n\nenter your saving throw values. Once again remember to include the '+' or '-':\n")

throws.append(input("Fortitude: "))
throws.append(input("Reflex: "))
throws.append(input("Will: "))

hp = input("\n\nenter creature hp\n")

speed = input("\n\nenter creature speed\n")

method = '1'

"""

"""
#enter through text document
if method == '2':
    # the desktop
    #file name to be created
    fileName = 'myAttacks.txt'
    exists = False
    while exists == False:
        try:
            f = open(myDir+fileName, 'x')
            f.close()
            exists = True
        except:
            fileName = input("sorry, "+fileName+" already exists, please enter a new name that doesn't already exist (include .txt at the end).\n")

    input("We've created a file called '"+fileName+"' on your desktop. Please write out each attack, seperated by pressing enter twice. When you're done, press enter here in the terminal.\n")
    f.open(myDir+fileName, 'r')
    attacks = convert2(f.read())
"""
"""
#enter through terminal
if method == '1':
    loop = int(input("\n\nhow many attacks does the creature have?\n"))
    for i in range(loop):
        attacks.append(input("\n\nenter attack "+str(i+1)+'\n'))

spells = input("\n\nEnter your creature's spells\n")

inventory = input("\n\nEnter your creature's inventory\n")

ps = input("\n\nEnter your post scriptum. This is for anything you want to add to the end of the page.\n\n")
"""
#endregion

outputName = input("\n\nplease name your pdf (don't include the .pdf at the end)\n")

doPdf()

pdf.output(myDir+outputName+'.pdf')

input("press enter to close program\n")