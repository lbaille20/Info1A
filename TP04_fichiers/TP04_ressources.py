"""TP4_ressources : Ressources pour le TP4"""

"""Exercice 2"""
L2=[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
"""Exercice 4"""
figures=["As","Roi","Dame","Valet"]
couleurs=["cœur","carreau","pique","trèfle"]
"""Exercice 5"""
L5=[7,6,4,3,1,1,9]
"""Exercice 6"""
L6=[[11,12],[23,24]]
"""Exercice 7"""
alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', \
          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

nom_code=[7, 21, 9, 4, 15, 22, 15, 14, 18, 15, 19, 19, 21, 13]

def mystere(a):
    k=0
    while alphabet[k]!=a:
        k+=1
    return k+1

texte_code=[15, 8, ' ', 19, 28, 23, 11, 18, 17, ' ',\
            6, "'", 8, 22, 23, ' ', 5, 18, 17]

texte_code2=[15, 8, ' ', 19, 28, 23, 11, 18, 17, ' ',\
            6, "'", 8, 22, 23, ' ', 5, 18, 17, ',', \
            ' ', 28, ' ', 4, ' ', 19, 4, 22, ' ', 7, \
            "'", 4, 21, 8, 23, 8, 22, ' ', 7, 8, 7, 4, 17, 22]


"""Exercice 8"""
L_aleat=[\
    56, 28, 91, 32, 34, 51, 64, 3, 26, 58, 29, 64, 32, 23, 99, 69, 72\
    , 99, 20, 36, 63, 50, 66, 82, 7, 1, 52, 56, 40, 22, 32, 97, 61, 89 \
    , 60, 95, 10, 3, 65, 60, 20, 39, 34, 3, 60, 36, 13, 6, 1, 91, 23, \
    25, 73, 62, 23, 79, 39, 19, 72, 80, 50, 5, 88, 12, 80, 81, 67, 14,\
    88, 25, 76, 70, 61, 78, 43, 4, 61, 36, 48, 36, 34, 67, 45, 69, 70, \
    75, 98, 30, 11, 71, 54, 53, 14, 95, 21, 19, 12, 76, 16, 91, 42, 13, \
    38, 29, 95, 21, 29, 88, 96, 87, 35, 52, 69, 48, 65, 59, 3, 2, 62, \
    37, 68, 11, 75, 88, 37, 83, 90, 54, 32, 52, 8, 93, 62, 30, 55, 18, \
    32, 36, 78, 26, 0, 26, 3, 63, 62, 66, 16, 71, 35, 25, 82, 99, 43, \
    51, 19, 11, 56, 27, 45, 92, 42, 54, 88, 56, 18, 74, 83, 10, 64, 15,\
    78, 81, 98, 38, 71, 73, 19, 42, 87, 55, 57, 77, 70, 19, 56, 68, 11,\
    43, 28, 51, 39, 19, 1, 86, 55, 40, 81, 18, 36, 48, 39, 17, 37, 37, \
    23, 41, 46, 15, 88, 91, 4, 72, 9, 7, 81, 32, 11, 41, 12, 7, 88, 21,\
    58, 15, 38, 82, 34, 66, 58, 48, 18, 82, 50, 80, 92, 81, 81, 57, 79,\
    97, 59, 13, 32, 89, 79, 43, 87, 70, 88, 27, 39, 65, 41, 41, 41, 40, \
    7, 85, 77, 66, 45, 87, 30, 89, 91, 94, 30, 1, 48, 22, 73, 74, 65, \
    65, 16, 74, 54, 64, 13, 95, 20, 47, 80, 93, 89, 17, 72, 3, 16, 98, \
    36, 60, 24, 54, 4, 79, 37, 25, 64, 42, 60, 79, 70, 57, 79, 85, 21, \
    31, 81, 97, 69, 62, 29, 30, 82, 31, 40, 52, 68, 72, 44, 2, 27, 46, \
    21, 26, 64, 42, 97, 86, 62, 94, 34, 11, 68, 17, 81, 37, 3, 9, 81, \
    77, 32, 28, 64, 34, 55, 31, 44, 45, 67, 31, 21, 76, 3, 18, 12, 13,\
    81, 79, 99, 89, 30, 30, 27, 55, 48, 43, 32, 18, 29, 28, 44, 23, 61,\
    88, 99, 18, 36, 16, 93, 58, 98, 66, 43, 21, 59, 49, 39, 16, 62, 91,\
    12, 66, 13, 53, 1, 16, 27, 20, 8, 14, 43, 10, 85, 25, 23, 55, 6, 58,\
    72, 22, 92, 88, 99, 22, 11, 12, 13, 42, 73, 84, 90, 73, 6, 34, 26, \
    57, 61, 10, 98, 7, 69, 26, 77, 84, 30, 13, 48, 49, 58, 56, 35, 91, \
    50, 50, 24, 58, 1, 1, 25, 57, 76, 32, 59, 49, 95, 96, 46, 39, 13, \
    77, 90, 56, 84, 4, 74, 61, 89, 40, 30, 93, 10, 65, 95, 51, 65, 52, \
    13, 73, 11, 16, 79, 4, 9, 45, 65, 53, 53, 24, 57, 98, 93, 67, 94,\
    95, 44, 56, 42, 1, 38, 30, 67, 58, 30, 92, 11, 50, 59, 44, 89, 84, \
    94, 83, 5, 32, 44, 81, 60, 77, 82, 5, 10, 46, 42, 28, 75, 16, 71, \
    20, 69, 98, 48, 27, 64, 82, 21, 72, 97, 75, 15, 30, 20, 54, 78, 6,\
    14, 13, 47, 90, 38, 67, 84, 82, 92, 65, 94, 82, 53, 19, 24, 92, 47,\
    58, 27, 75, 70, 0, 89, 22, 60, 2, 87, 36, 87, 85, 22, 94, 87, 5, 72,\
    84, 4, 66, 64, 15, 54, 50, 93, 16, 2, 38, 15, 48, 42, 13, 38, 30, \
    98, 93, 98, 45, 85, 56, 72, 72, 11, 67, 51, 22, 96, 68, 96, 17, \
    81, 23, 39, 66, 65, 39, 14, 93, 61, 21, 24, 21, 48, 59, 54, 28, \
    75, 13, 43, 80, 85, 32, 36, 36, 27, 85, 12, 46, 79, 3, 17, 89, 5,\
    26, 95, 3, 35, 74, 90, 18, 15, 58, 74, 83, 18, 56, 76, 12, 14, 44,\
    82, 25, 37, 14, 65, 40, 88, 86, 78, 84, 45, 30, 69, 95, 65, 30, \
    62, 30, 90, 68, 22, 59, 97, 21, 79, 63, 13, 77, 87, 81, 26, 90, \
    85, 51, 74, 69, 32, 71, 50, 92, 17, 25, 24, 12, 1, 69, 47, 64, \
    84, 64, 43, 41, 11, 53, 36, 73, 83, 77, 29, 31, 96, 38, 17, 1, \
    58, 1, 9, 88, 57, 96, 94, 74, 91, 75, 31, 77, 24, 23, 4, 40, \
    17, 25, 40, 10, 76, 92, 94, 61, 91, 41, 85, 27, 16, 51, 0, 2,\
    29, 76, 74, 96, 1, 90, 89, 34, 43, 16, 80, 46, 97, 44, 43, 79,\
    53, 25, 39, 74, 65, 73, 51, 46, 4, 85, 41, 24, 61, 30, 49, 89,\
    95, 85, 94, 66, 87, 59, 66, 67, 41, 64, 10, 78, 94, 91, 61, \
    48, 93, 98, 86, 92, 56, 65, 2, 81, 17, 37, 42, 56, 47, 56, \
    34, 18, 62, 28, 99, 43, 41, 7, 34, 73, 39, 1, 5, 49, 21, 0,\
    75, 48, 98, 35, 27, 89, 68, 34, 53, 91, 84, 87, 15, 6, 90, \
    26, 43, 15, 65, 29, 2, 6, 2, 23, 20, 34, 69, 65, 16, 65, 86,\
    5, 11, 83, 72, 97, 69, 8, 20, 20, 88, 78, 5, 31, 80, 29, 80,\
    93, 71, 69, 17, 63, 21, 74, 62, 1, 53, 86, 91, 63, 28, 82, 9,\
    34, 60, 38, 3, 43, 75, 97, 53, 85, 58, 87, 35, 64, 26, 41, 10, \
    13, 73, 18, 8, 90, 12, 4, 9, 42, 16, 48, 82, 6, 11, 76, 99, 69,\
    92, 36, 0, 43, 40, 99, 62, 66, 93, 24, 30, 9, 93, 42, 83, 12, 29,\
    58, 20, 18, 72, 94, 28, 43, 88, 35, 56, 9, 61, 71, 70, 22, 25, 78,\
    37, 65, 77, 12, 17, 69, 17, 65, 54, 8, 90, 98, 63, 57, 95, 65, 5,\
    40, 38, 16, 77, 13, 86, 37, 11, 42, 50, 16, 41, 11, 18, 46]

"""Utilitaire pour vider le cache de TP4_Ressources.py"""
def vide_cache():
    import os
    emplacement_cache=os.path.join(os.getcwd(),"__pycache__")
    contenu_cache=os.listdir(emplacement_cache)
    for file in contenu_cache:
        os.remove(os.path.join(emplacement_cache,file))
