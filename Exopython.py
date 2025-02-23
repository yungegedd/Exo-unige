import random

from utils import exercice , formatter_sudoku ,generer_personnes,generer_resultats, obtenir_sudoku_valide

@exercice
def ExerxciceIA():
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

@exercice
def exercice1():
    Nom = input("Entrez votre nom : ")
    Prenom = input("Entrez votre prénom : ")
    Date_de_naissance = input("Entrez votre date de naissance : ")
    print(f"Bienvenue {Prenom} {Nom} ! Vous etes né le {Date_de_naissance}.")

@exercice
def exercice2():
    """
    This function calculates the squares of numbers from 1 to 9 and prints them.

    Parameters:
    None

    Returns:
    None
    """
    Nombres = list(range(1,10))
    carres=[]

    for i in Nombres:
        carres.append(i*i)
    print(carres)

    # plus court
    print("\n".join([f"{i}:{s} for i,s in zip(Nombres,carres)"]))

@exercice
def exercice3():
    nombres = list(range(0,50))
    pairs = []
    impairs = []
    for i in nombres:
        if i%2==0:
            pairs.append(i)
        else:
            impairs.append(i) 
    print(f"pairs : {pairs}")
    print(f"impairs : {impairs}")

@exercice
def exercice5():
    a = [2,3]
    b = a
    print(a)
    print(b)

    b[0] = 1
    print(a)
    print(b)  

    a =[5,6]
    b[0] = 10
    print(a)
    print(b)

    # dans la premiere partie a et b sont tjrs les memes ensuite a =[1,3] et b = [1,3]
    # ensuite a = [5,6] et b = [10,3]


@exercice
def exercice6():    
    liste_de_liste = [[93, 49, 71], [36, 83, 53], [66, 32, 51]]
    liste_applatie = []
    for liste in liste_de_liste:
        liste_applatie += liste

    print(f"liste de liste : {liste_de_liste}")
    print(f"liste aplatie : {liste_applatie}")  


@exercice
def exercice7():





# ExerxciceIA()
# exercice1()
#exercice2()
# exercice3()
exercice5()
exercice6()
exercice7()