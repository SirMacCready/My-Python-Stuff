import time, sys
Valeur = 0
ValeurAugmente = True

try:
    while True:
        print(' ' *Valeur, end= ' ')
        print('IERWNEIJNIEWRNIEWURJWEIURJIEWURJWIUEJRi')
        time.sleep(0.00002)

        if ValeurAugmente:

            Valeur = Valeur + 1
            if Valeur == 20:

                ValeurAugmente = False

        else :
            Valeur = Valeur - 1
            if Valeur == 0:
                ValeurAugmente = True
except KeyboardInterrupt:
    sys.exit()
