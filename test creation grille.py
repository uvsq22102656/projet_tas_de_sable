import random as rd
import tkinter as tk
#CONSTANTES

#taille de la grille
L = 4
#hauteur de la grille
HEIGHT = 500
#largeur de la grille
WIDTH = 500

#variable globale
grille = []


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
            nb = rd.randint(0,3)
            case = canvas.create_text((i,j), text=str(nb))
            grille[i][j] = case


# partie pricipale

# création widgets
racine = tk.Tk() # Création de la fenêtre racine
bouton = tk.Button(racine, text="initialisation", command=initialisation)
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH)
canvas.create_text(100,500, text="hello")

#placement des widgets
bouton.grid(column=0, row=1)
canvas.grid(column=0, row=0)

#initialisation()

#boucle principale
racine.mainloop()