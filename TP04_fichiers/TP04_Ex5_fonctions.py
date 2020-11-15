#fonctions spécifiques pour l'exercice 5

def etat(Lvar):
    print("Valeurs des listes en mémoire :")
    for var in Lvar:
        print(var)

def mem(Lvar):
    print("Adresses des listes en mémoire :")
    for var in Lvar:
        print(hex(id(var)))
