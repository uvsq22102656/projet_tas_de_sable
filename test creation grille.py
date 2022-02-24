import random as rd
import tkinter as tk
#CONSTANTES

#taille de la grille
L = 4
#hauteur de la grille
HAUTEUR = 500
#largeur de la grille
LARGEUR = 500

#variable globale
grille = [] #contient uniquement les id des cases pour modif param. graphiques
"""Q : créer une autre liste qui stock le nb de grains de sable ?
(oui si operation sur valeur necessaire)
[sinon obligé de recuperer valeur dans str du rectangle = galere ?]"""
l_case = LARGEUR//L

####################
# fonctions

def initialisation():
    """initialisation du terrain :
    * creation de la grille avec toutes les cases à 0"""
    global grille
    for i in range(L):
        grille.append([0]*L)

    for i in range(L):
        for j in range(L):
            case = canvas.create_text((i*l_case,j*l_case), text=0)
            grille[i][j] = case #recuperation id pour modif +tard


def insert_valeur():
    """insertion des valeurs dans la grille à la place des 0"""
    global grille
    for i in range(L):
        for j in range(L):
            nb = rd.randint(0,3) #utiliser rd.uniform ?
            case = canvas.create_text((i*l_case,j*l_case), text=str(nb))
            grille[i][j] = case


# partie pricipale

# création widgets
racine = tk.Tk() # Création de la fenêtre racine
bouton = tk.Button(racine, text="initialisation", command=initialisation)
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR)

#placement des widgets
bouton.grid(column=0, row=1)
canvas.grid(column=0, row=0)

#initialisation()

#boucle principale
racine.mainloop()