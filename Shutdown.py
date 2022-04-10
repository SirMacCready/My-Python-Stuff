import webbrowser, os , time
print("Entrez la durée du compte à rebours en secondes : ")
a = input()
print('Début du compte à rebours')
time.sleep(a)
os.system("shutdown /s /t 1")
