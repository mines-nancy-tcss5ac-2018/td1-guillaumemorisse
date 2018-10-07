# -*- coding: utf-8 -*-
"""
Created on Sun Oct 07 15:53:04 2018

@author: Guillaume MORISSE
"""

def reverse(n) :
    "prend en argument un int et renvoie un int correspondant au nombre avec l'odre des chiffres inversé"
    rev = str()
    for i in str(n):
        rev = i + rev
    return int(rev)
    
    
def test_lynchrell(n) :
    "pour un nombre donné réalise le test donné problème 55 en énoncé pour vérifier si'il s'agit d'un nombre de lynchrell, renvoie un booléen correspondant au résultat"
    m=n
    test = True
    compteur = 0
    while compteur < 50 and test :
        if m + reverse(m) == reverse (m + reverse(m)): #si le nombre obtenu est un palyndrome alors n est un lynchrell
            test = False
        compteur += 1
        m = m + reverse (m)
    return test
    
def solve(n) :
    "renvoie le nombre d'entiers inférieurs à n qui sont des  nombres de lynchrell"
    N = 0
    for i in range(n) :
        if test_lynchrell(i):
             N += 1
    return N
    

assert test_lynchrell(349) == False

print solve(10000)
