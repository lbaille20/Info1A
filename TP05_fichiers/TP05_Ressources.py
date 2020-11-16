"""Ressources pour le TP5"""

def temps_attente_R():
    from random import randint
    s=0
    n=0
    while s<12:
        s=sum([randint(1,6) for k in range(3)])
        n+=1
    return n

def f_R(n):
    L=[]
    for k in range(n):
        L.append(2**k)
    return L
