#########################################
# DLMP groupe 6
# NOUVEAU Maxence
# DERWEL Nathan 
# VOLIVERT Coline
# https://github.com/uvsq-info/l1-python
#########################################

#########################
# import des librairies
import tkinter as tk
import random as rd

#########################
#CONSTANTES

#taille de la grille
L = 4
#hauteur de la grille
HEIGHT = 500
#largeur de la grille
WIDTH = 500


#########################
# partie pricipale

# création widgets
racine = tk.Tk()
racine.title("projet tas de sable")
bouton = tk.Button(racine, text="initialisation",)
canvas = tk.Canvas(racine, height=HEIGHT, width=WIDTH)

#placement des widgets
bouton.grid(column=0, row=1)
canvas.grid(column=0, row=0)

        
#boucle principale
racine.mainloop()