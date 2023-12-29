"""
#Exercice 3.6.1
taille = int(input("taille de la liste :"))
liste = []
for long in range(0,taille):
    liste.append(input())
print(liste)
"""

"""
#Exercice 3.6.2
listenb = input()
nombres = "0123456789"
somme = 0
for donnee in listenb:
    if donnee in nombres:
        somme += int(donnee)
print(somme)
"""

"""
#Exercice 3.6.3
chaine = input()
max = 0
for chara in chaine:
    if len(chara) > max:
        max = len(chara)
print(max)
"""

"""
#Exercice 3.6.4
chaine = input()
voyelles = "aeiouAEIOU"
newchaine = ""
for chara in chaine:
    if chara in voyelles:
        newchaine += "*"
    else:
        newchaine += chara
print(newchaine)
"""

"""
#Exercice 3.6.5
phrase = input()
mots = phrase.split()
for mot in mots:
    print(mot)
"""
"""
liste_entiers = input("Entrez une liste d'entiers (séparés par des espaces) : ").split()

valeur_recherchee = input("Entrez la valeur à rechercher : ")

indices = []

for i in range(len(liste_entiers)):
    if liste_entiers[i] == valeur_recherchee:
        indices.append(i)

if indices:
    print(f"La valeur {valeur_recherchee} apparaît aux indices : {indices}")
else:
    print(f"La valeur {valeur_recherchee} n'apparaît pas dans la liste.")
"""
