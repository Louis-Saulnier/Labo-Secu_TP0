print("Veuillez choisir un nombre.")

n = input()
diviseur = []

for i in range(1, int(n)) :
    if (int(n) % (i) == 0) :
        diviseur.append(i)
        print("Diviseur " + str(len(diviseur)) + ") " + str(i))