def traitement_proposition(lettre, mot, trouvees):
    #rappel : mot et trouvees sont deux chaînes de caractères de même longueur
    trouvees_nouvelle = ""
    succes = False # restera à False, sauf si on trouve une nouvelle lettre
    for k in range(len(mot)):
        if lettre == mot[k] and trouvees[k] == '_': #si la lettre proposée est dans le mot à la position k
                                                    # et n'a pas été déjà trouvée
            trouvees_nouvelle += mot[k]
            succes = True
        else:                                       #sinon, on reproduit la chaîne trouvee à l'identique en position k
            trouvees_nouvelle += trouvees[k]
    return trouvees_nouvelle, succes

## https://python.sdv.univ-paris-diderot.fr/14_creation_modules/
if __name__ == "__main__":
    """tests"""
    mot = "anaconda"
    trouvees = len(mot) * "_"
    lettre = "a"
    trouvees, s = traitement_proposition(lettre, mot, trouvees)
    print(trouvees, s)

    lettre = "a"
    trouvees, s = traitement_proposition(lettre, mot, trouvees)
    print(trouvees, s)

    lettre = "e"
    trouvees, s = traitement_proposition(lettre, mot, trouvees)
    print(trouvees, s)

    lettre = "n"
    trouvees, s = traitement_proposition(lettre, mot, trouvees)
    print(trouvees, s)
