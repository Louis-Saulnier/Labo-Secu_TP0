patients = []

while (len(patients) != 5) :
    print("Veuillez rentrer le nom d'un patient voulant rejoindre la liste d'attente.")

    patient = input()

    patients.append(patient)

print("La liste d'attente est pleine.")
print("Voici la liste d'attente:")

for patient in patients :
    print(str(patients.index(patient)) + ") " + patient)

while (len(patients) != 0) :
    print("Veuillez rentrer le numéro d'arivée dans la liste d'attente d'un patient a retirer de la liste d'attente.")

    index = input()

    try :
        patients.pop(int(index))
    except:
        print("Ce numéro n'est attribué à aucun patient.")