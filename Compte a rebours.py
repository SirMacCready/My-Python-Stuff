import time
#Compte a rebours
print("Veuillez Enter la durée du minuteur")
a=input()
while a != 0 :
    print(a)
    a = a-1
    time.sleep(1)

print("Bonne Année !")
