import webbrowser, os , time
print("Entrez la durée du compte à rebours en secondes : ")
a = input()
print('Début du compte à rebours')
while a !=0:
    print(a)
    a=int(a) -1
    time.sleep(int(1))
os.system("shutdown /s /t 1")
