from fpdf import FPDF
import os.path
from os import path

#vars
pdf = FPDF('P', 'mm', 'letter')

name = ""
traits = []

perception = ''
senses = ""

skills = ""

abNames = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']
abScrs = []

ac = ''

throws = []

speed = ''

attacks = []

f = open("SaveDirectory.txt", 'r')
myDir = f.read()
f.close()


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

    pdf.set_font_size(26)
    #line break
    pdf.multi_cell(w=20, h=10, txt="\n\n", ln=1)


    #text
    pdf.cell(200, 10, name, 1, 1)

    #font size
    pdf.set_font_size(12)

    #traits
    for i in range(len(traits)):
        pdf.cell(25, 10, traits[i], 1, 0)
    
    #line break
    pdf.multi_cell(w=20, h=10, txt="\n", ln=1)

    #stats
    pdf.multi_cell(0, 10, "Perception +"+perception+'; '+senses, ln=1)
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
    pdf.cell(10, 10, "HP 24", ln=1)
    #vertical line
    pdf.cell(10, 10, '-'*100, ln=1)
    pdf.cell(10, 10, "Speed: "+speed, ln=1)
    #print the attacks (can print as many as you want)
    for i in range(len(attacks)):
        pdf.multi_cell(0, 5, '\n'+attacks[i], ln=1)

    """ 
    pdf.cell(10, 10, attacks[0], ln=1)
    pdf.cell(10, 10, attacks[1], ln=1)
    pdf.cell(10, 10, "", ln=1)
    pdf.cell(10, 10, "", ln=1)
    pdf.cell(10, 10, "", ln=1)
    pdf.cell(10, 10, "", ln=1)
 """


#program
input("Welcome to Pathfinder creature maker! Press Enter to begin!\n")

name = input("What would you like to name your Creature?\n")
traits = convert(input("What traits does your creature have? Please seperate each item by a space and comma.\n"))

perception = input("Perception? Be sure to add the '+' or '-'.\n")
senses = input("enter the senses\n")

skills = input("enter your creature's skills.\n")

print("enter your ability score bonuses (ex: +3). Be sure to include the '+' or '-':\n\n")
for i in range(len(abNames)):
    abScrs.append(input(abNames[i]+' '))

ac = input("enter creature AC.\n")

print("enter your saving throw values. Once again remember to include the '+' or '-':\n")

throws.append(input("Fortitude: "))
throws.append(input("Reflex: "))
throws.append(input("Will: "))

input("enter creature speed\n")

method = input("would you like to enter the attacks through the terminal or through a txt document that will be created on your desktop?\n(1) - terminal\n(2) - txt document\n")


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

#enter through terminal
if method == '1':
    loop = int(input("how many attacks does the creature have?\n"))
    for i in range(loop):
        attacks.append(input("enter attack "+str(i+1)+'\n'))


doPdf()

outputName = input("please name your pdf (don't include the .pdf at the end)\n")

pdf.output(myDir+outputName+'.pdf')