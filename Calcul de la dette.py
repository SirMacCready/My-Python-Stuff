while True :
    print("Veuillez entrer le placement initial")
    Sommedebase = input()
    print("Veuillez entrer le taux d'intérêt")
    Taux = input()
    print("Veuillez entrer le nombre d'années")
    Annees = input()
    print("Veuillez entrer le montant du Versements annuel")
    Placement = input()
    interet = float(Sommedebase) * float(Taux) * float(Annees) / 100 + float(Placement) * float(Annees)
    Sommesimple = float(Sommedebase) + float(interet)
    print("l'intérêt Simple gagné est de : " + str(interet))
    print("L'intérêt Simple est de : " + str(Sommesimple))
    a=0
    while a != float(Annees) :
        Taux2 = float(Sommedebase) *float(Taux) / 100 + float(Placement)
        Sommedebase = float(Sommedebase) + float(Taux2)
        a = a + 1
    print("L'intérêt composé est de : " + str(Sommedebase))
    Intcomp = float(Taux2) * float(Annees)
    print('')
