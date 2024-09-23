patients = []

while (len(patients) != 5) :
    print("Veuillez rentrer le nom d'un patient voulant rejoindre la liste d'attente.")

    patient = input()

    patients.append(patient)

print("La liste d'attente est pleine.")
print("Voici la liste d'attente:")

for patient in patients :
    print(patient)

while (len(patients) != 0) :
    print("Veuillez rentrer le nom d'un patient a supprimer de la liste d'attente.")

    patient = input()

    if patient in patients:
        patients.remove(patient)
    else :
        print("Cette personne ne fait pas parti de la liste d'attente.")