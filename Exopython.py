# Exercice 1 : Indentation et Boucles
# Écrire un programme qui affiche les nombres de 1 à 10.
#  Pour chaque nombre, afficher "pair" s'il est pair et "impair" sinon.

for i in range(1,11):
    if i%2==0:
        print("i=",i ,"est pair")
    else:
        print("i=",i ,"est impair")    

# Exercice 2 : Utilisation des types de base
# Écrire un programme qui demande à
#  l'utilisateur de saisir un nombre entier.
#   Le programme doit ensuite afficher ce nombre, 
#   son double et son carré.      

a = int(input("Entrez un nombre entier : "))
print(f"le nombre est {a} et son double est {2*a}, son carré est {a*a}") 

#Exercice 3 : Opérateurs et contrôle du flot
# Écrire un programme 
# qui prend une chaîne de caractères en entrée et vérifie
#  si elle contient au moins un caractère numérique.

chaine = input("Entrez une chaine de caractères : ")
for i in chaine:
    if i.isdigit():
        print("La chaine contient un caractère numérique")
        break
    else:
        print("La chaine ne contient pas de caractère numérique")
        break

chaine = input("Saisissez une chaîne de caractères: ")
contient_chiffre = any(char.isdigit() for char in chaine)
if contient_chiffre:
    print("La chaîne contient au moins un chiffre.")
else:
    print("La chaîne ne contient aucun chiffre.")

#Exercice 4 : 
# Écrire un programme qui prend le prénom et le nom 
# d'une personne en entrée et affiche 
# un message de bienvenue formaté avec les f-strings.

Nom = input("Entrez votre nom : ")
Prenom = input("Entrez votre prénom : ")
print(f"Bienvenue {Prenom} {Nom} !")




