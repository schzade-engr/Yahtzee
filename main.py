import random
#=======================
# Yahtzee Game
# Rules: 5 dice, 3 throws
# Yahtzee combos:
# https://www.memory-improvement-tips.com/support-files/yahtzee-score-sheet-large.pdf
# Description: This game manages one player, each person who is playing this game keeps
# their own sheet. For a new game, restart the program.
#
# Author: STaylor (credit to Camryn for the ideas and snatched a bit of code... thanks!)
# ================================
list_of_dies = []
#constants:
NumRolls=3
initialRR = 4
#functions:
def rollDie(whichReRoll, list_of_dies):
    print(list_of_dies)
    die1 = list_of_dies[0]
    die2 = list_of_dies[1]
    die3 = list_of_dies[2]
    die4 = list_of_dies[3]
    die5 = list_of_dies[4]
    
    if whichReRoll[0] == 1:
        die1 = random.randint(1,6)
    if whichReRoll[1] == 1:
        die2 = random.randint(1,6)
    if whichReRoll[2] == 1:
        die3 = random.randint(1,6)
    if whichReRoll[3] == 1:
        die4 = random.randint(1,6)
    if whichReRoll[4] == 1:
        die5 = random.randint(1,6)
    
    list_of_dies = [die1, die2, die3, die4, die5]
    return(list_of_dies)
def askReRoll():
    print("For each reroll response, enter 1 if you want to reroll")
    print(" enter 0 if you don't")
    
    rr[0] = int(input("Do you want to reroll die 1? "))
    rr[1] = int(input("Do you want to reroll die 2? "))
    rr[2] = int(input("Do you want to reroll die 3? "))
    rr[3] = int(input("Do you want to reroll die 4? "))
    rr[4] = int(input("Do you want to reroll die 5? "))
    
    return(rr)

#main code    
    
print("Greetings and salutations!")
# promt user to give a name
name = input("What is your name? ")
print("Nice to meet you " + name)
print("lets play Yahtzee!")

list_of_dies = [1, 1, 1, 1, 1]
rr = [1, 1, 1, 1, 1]
# these variables define the the numbers the dice roll

for i in range(3):
    if i == 0:
        list_of_dies = rollDie(rr, list_of_dies)
    if i > 0 and i < 3:
        ask = input("Do you want to reroll?")
        if (ask == "yes"):
            rr = askReRoll()
            list_of_dies = rollDie(rr, list_of_dies)
    print(list_of_dies)






