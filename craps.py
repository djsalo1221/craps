from random import randint           #random, randint

print('come-out')               # vague output
firstDie = randint(1, 6)               #vague variable name
secondDie = randint(1, 6)                #vague variable name
firstRoll = firstDie + secondDie                 #vague assignment
print(firstRoll)                            #vague variable
if firstRoll == 7 or firstRoll == 11:
    print('You win!')                       
elif firstRoll == 2 or firstRoll == 3 or firstRoll == 12:
    print('Craps, you lose.')       
else:
    print('The point is', firstRoll)      # vague variable name
    firstDie = randint(1, 6)          #vague variable name
    secondDie = randint(1, 6)         #vague variable name
    secondRoll = firstDie + secondDie                #vague assignment
    print(secondRoll)
    while secondRoll != firstRoll and secondRoll != 7:
        firstDie = randint(1, 6)       #vague variable name
        secondDie = randint(1, 6)       #vague variable name
        secondRoll = firstDie + secondDie
        print(secondRoll)
    if secondRoll == 7:
        print('Seven out, you lose.')
    else:
        print('Pass, you win!')
