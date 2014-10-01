from random import randint           #random, randint

print('come-out')               # vague output
r1 = randint(1, 6)               #vague variable name
r2 = randint(1, 6)                #vague variable name
v = r1 + r2                 #vague assignment
print(v)                            #vague variable
if v == 7 or v == 11:
    print('You win!')                       
elif v == 2 or v == 3 or v == 12:
    print('Craps, you lose.')       
else:
    print('The point is', v)      # vague variable name
    r1 = randint(1, 6)          #vague variable name
    r2 = randint(1, 6)         #vague variable name
    w = r1 + r2                #vague assignment
    print(w)
    while w != v and w != 7:
        r1 = randint(1, 6)       #vague variable name
        r2 = randint(1, 6)       #vague variable name
        w = r1 + r2
        print(w)
    if w == 7:
        print('Seven out, you lose.')
    else:
        print('Pass, you win!')
