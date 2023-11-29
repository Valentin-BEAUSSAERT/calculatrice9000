# Récupération et conversion des entrées
nombre1 = input("Entre le premier nombre : \n").replace(',', '.')
nombre2 = input("Entre le deuxième nombre : \n").replace(',', '.')

try:
    nombre1 = float(nombre1)
    nombre2 = float(nombre2)
except ValueError:
    print("Entrée non valide. Veuillez entrer un nombre.")
    exit()

operation = input("Renseigne l'opération (somme, soustraction, produit ou quotient) \n")

# Pour l'addition
if operation == "somme":
    somme = nombre1 + nombre2
    print(f"La somme de {nombre1} et {nombre2} est égal à {somme}")

# Pour la soustraction
elif operation == "soustraction":
    difference = nombre1 - nombre2
    print(f"La différence de {nombre1} - {nombre2} est égal à {difference}")

# Pour le produit
elif operation == "produit":
    produit = nombre1 * nombre2
    print(f"Le produit de {nombre1} par {nombre2} est égal à {produit}")

# Pour le quotient
elif operation == "quotient":
    if nombre2 != 0:
        quotient = nombre1 / nombre2
        print(f"Le quotient de {nombre1} par {nombre2} est égal à {quotient}")
    else:
        print("Erreur : Division par zéro.")
else:
    print("Opération non reconnue.")

