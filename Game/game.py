# savegame
import save

# imports
import random

# vars
attack = ''
maxHP = save.maxHP
currentHP = save.currentHP
currentXP = save.currentXP
currentLVL = save.currentLVL
money = save.money

def reset():
    global currentHP
    global maxHP
    global currentXP
    global currentLVL
    maxHP = 10
    currentHP = 10
    currentXP = 0
    currentLVL = 1

def enemy1():
    global currentHP

    print("You encountered a Goblin. You'll now fight it.")

    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        currentHP -= 1
    elif randomNumber == 2:
        currentHP -= 3
    elif randomNumber == 3:
        currentHP -= 5

def enemy2():
    global currentHP

    print("You encountered a Skeleton. You'll now fight it.")

    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        currentHP -= 10
    elif randomNumber == 2:
        currentHP -= 30
    elif randomNumber == 3:
        currentHP -= 50

def enemy3():
    global currentHP

    print("You encountered a Witch. You'll now fight it.")

    randomNumber = random.randint(1, 3)

    if randomNumber == 1:
        currentHP -= 100
    elif randomNumber == 2:
        currentHP -= 300
    elif randomNumber == 3:
        currentHP -= 500

def game():
    global currentHP
    global maxHP
    global currentXP
    global currentLVL
    global money

    # level up when there is enough xp to level up.
    if currentXP == currentLVL * 100:
        currentXP -= currentLVL * 100
        currentLVL += 1
        maxHP = 10 + currentLVL
        print("LEVEL UP!!!")

    if currentHP > 0:
        print('..................................................\nHP = ' + str(currentHP) + '\nmoney = ' + str(money) + '\nLVL = ' + str(currentLVL) + '\nXP = ' +  str(currentXP))
        action = input('If you want to fight, Press f\nIf you want to heal ($15), Press h\nIf you want to stop playing, Press e\nIf you want to save, Press s\n')
        if action == 'f':
            enemy = input('What enemy do you want to fight?\n[1] Goblin\n[2] Skeleton\n[3] Witch\n')
            if enemy == '1':
                enemy1()
                currentXP += random.randint(10, 100)
                money += random.randint(5,20)
            if enemy == '2':
                enemy2()
                currentXP += random.randint(100, 1000)
                money += random.randint(50,200)
            if enemy == '3':
                enemy3()
                currentXP += random.randint(1000, 10000)
                money += random.randint(500,2000)
        elif action == 'h':
            if money >= 20:
                currentHP = maxHP
                money -= 20
            else:
                print('Too low on money, earn some more first.')
                game()
        elif action == 'e':
            exit()
        elif action == 's':
            f = open('PersonalProjects/Game/save.py', 'w')
            f.write('maxHP = ' + str(maxHP) + '\n')
            f.write('currentHP = ' + str(currentHP) + '\n')
            f.write('currentXP = ' + str(currentXP) + '\n')
            f.write('currentLVL = ' + str(currentLVL) + '\n')
            f.write('money = ' + str(money) + '\n')
            f.close()
        elif action == 'reset':
            reset()
        else:
            print('Invalid input.')
        game()
    else:
        print('You died. Your progress has been reset.')
        reset()
        game()

game()