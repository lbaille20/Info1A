## importation des fonctions gérant les affichages
import TP07_Ex09_affichages_fonctions as maj_aff
import matplotlib.pyplot as plt

plt.ion()

## initialisation de l'affichage et des variables permettant de le gérer
fig, ax, texte_affiche, elements_dessin = maj_aff.init()

##importation de la fonction traitement_proposition
from TP07_Ex09_traitement_proposition import traitement_proposition

## programme principal
import random
    
#Ouverture du fichier contenant la liste de mots à découvrir           
f = open("TP07_Ex09_liste_mots.txt", "r")
liste = f.readlines()
liste = [e.strip("\n") for e in liste]
f.close()
#print(liste)

#Tirage au sort du mot à découvrir
mot = random.choice(liste)
## print(mot)  ## on peut décommenter si on veut connaître à l'avance le mot à trouver

#Initialisation de la variable trouvees
#[chaîne de caractères de même longueur que le mot à trouver,
#dans laquelle les lettres non encore trouvées sont remplacées par "_"]
trouvees = len(mot) * "_"
nombre_echecs = 0

## mise à jour du texte affiché
maj_aff.update_texte(fig, texte_affiche, trouvees)

while (not trouvees == mot) and nombre_echecs < 12:
    proposition = input("Entrer une lettre (12 essais au maximum):\n")
    trouvees, succes = traitement_proposition(proposition, mot, trouvees)
    print(trouvees, succes)
    if not succes:
        maj_aff.update_fig(fig, elements_dessin, nombre_echecs)
        nombre_echecs += 1
    maj_aff.update_texte(fig, texte_affiche, trouvees)

maj_aff.update_final(fig, ax, mot, elements_dessin, nombre_echecs)
