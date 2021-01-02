#la fonction analyse_proposition...

def traitement_proposition(lettre, mot, trouvees):
    #rappel : mot et trouve sont deux chaînes de caractères de même longueur
    trouvees_nouveau = ""
    succes = False #restera à False, sauf si on trouve une nouvelle lettre
    for k in range(len(mot)):
        if trouvees[k] == mot[k]: #cette lettre du mot a déjà été trouvée
            trouvees_nouveau += mot[k]
        else: #la lettre du mot n'a été précédemment trouvée
            if mot[k] == lettre:
                succes = True
                trouvees_nouveau += mot[k]
            else:
                trouvees_nouveau += "_"
    return trouvees_nouveau, succes


## https://python.sdv.univ-paris-diderot.fr/14_creation_modules/
if __name__ == "__main__":
    """tests"""
    mot="python"
    trouve=len(mot)*"-"
    lettre="o"
    trouve, s = analyse_proposition(lettre, mot,trouve)
    print(trouve,s)

    lettre="o"
    trouve, s = analyse_proposition(lettre, mot,trouve)
    print(trouve, s)

    lettre = "e"
    trouve, s = analyse_proposition(lettre, mot,trouve)
    print(trouve, s)
    
