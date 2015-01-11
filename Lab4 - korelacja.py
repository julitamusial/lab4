# -*- coding: cp1250 -*-
#Korelacja Pearsona

from math import sqrt
from numpy import corrcoef

users = {
        "Ania": 
            {"Blues Traveler": 1.,
            "Broken Bells": 1.5,
            "Norah Jones": 2,
            "Deadmau5": 2.5,
            "Phoenix": 3.0,
            "Slightly Stoopid": .5,
            "The Strokes": 0.0,
            "Vampire Weekend": 2.0},
         "Bonia":
            {"Blues Traveler": 4.0,
            "Broken Bells": 4.5, 
            "Norah Jones": 5.0,
            "Deadmau5": 5.5, 
            "Phoenix": 6.0, 
            "Slightly Stoopid": 3.5, 
            "The Strokes": 2.0,
            "Vampire Weekend": 5.0}
        }

        
def manhattan(rating1, rating2):
    
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają… wspólnych elementów"""
       
    # TODO: wpisz kod
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    odleglosc = 0
    udaloSiePorownac = False

    for klucz in klucze1:
        if klucz in rating2.keys():
            udaloSiePorownac = True
            odleglosc = odleglosc + abs(rating2[klucz] - rating1[klucz])

    if (udaloSiePorownac==True):
        return odleglosc
    else:
        return -1

#Korelacja Pearsona
def pearson(rating1, rating2):
    korelacja = 0
    klucze1 = rating1.keys()
    klucze2 = rating2.keys()
    
    wartosciX = rating1.values()
    wartosciY= rating2.values()

    sumaX = 0
    sumaY = 0
    sumaIloczyn = 0
    sumaKwadratX = 0
    sumaKwadratY = 0

    for i in xrange(0, len(wartosciX)):
        sumaIloczyn = sumaIloczyn + wartosciX[i]*wartosciY[i]
        sumaX = sumaX + wartosciX[i]
        sumaY = sumaY + wartosciY[i]
        sumaKwadratX = sumaKwadratX + wartosciX[i]**2
        sumaKwadratY = sumaKwadratY + wartosciY[i]**2
    korelacja = (sumaIloczyn - ((sumaX * sumaY)/len(wartosciX)))/(sqrt(sumaKwadratX - (sumaX**2/len(wartosciX))) * sqrt(sumaKwadratY - (sumaY**2/len(wartosciY))))
    return korelacja

print pearson(users["Ania"], users["Bonia"])

#Korelacja Perasona - Numpy                                                                   
def pearsonNumpy(rating1, rating2):
    
    wartosciX = rating1.values()
    wartosciY = rating2.values()
    

    pearsonNumpy = corrcoef(wartosciX, wartosciY)
    korelacja = pearsonNumpy[1,0]
    return korelacja

print pearsonNumpy(users["Ania"], users["Bonia"])
