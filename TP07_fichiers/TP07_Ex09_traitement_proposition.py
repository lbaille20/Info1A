def traitement_proposition(proposition, mot, trouvees):
    trouvees_nouvelle, succes = trouvees, False
    return trouvees_nouvelle, succes


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
    
