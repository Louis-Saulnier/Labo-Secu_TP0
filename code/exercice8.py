import random

rnd = random.randint(1, 100)
hasFound = False
nTry = 0

print("Trouvez le nombre secret (entre 1 et 100)")

while (hasFound == False) :
    nTry+=1
    guess = input()

    if (int(guess) > rnd) :
        print("Plus petit")
    elif (int(guess) < rnd) :
        print("Plus grand")
    elif (int(guess) == rnd) :
        print("Vous avez gagné en " + str(nTry) + " coups !")
        hasFound = True