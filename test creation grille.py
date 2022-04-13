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
nb_clics = 0
nb = 0

####################
# fonctions

def initialisation():
    """initialisation du terrain :
    - creation de la grille avec toutes les cases à 0"""
    global grille, nb_clics, nb
    if nb_clics == 0:
        for i in range(L):
            grille.append([0]*L)
        for i in range(L):
            for j in range(L):
                rect = canvas.create_rectangle((i*l_case,j*l_case), ((i+1)*l_case,(j+1)*l_case),
                        fill='lightgoldenrod')
                case = canvas.create_text((i*l_case+l_case//2,j*l_case+l_case//2), text="0")
                grille[i][j] = case #recuperation id pour modif +tard
        nb_clics = 1

    else:
        insert_valeur(3) #configuration stable


def insert_valeur(n):
    """insertion des valeurs comprises entre 0 et n dans la grille à la place des 0"""
    global grille, case
    canvas.delete("all")
    liste_coul = ['lightgoldenrod','gold', 'goldenrod','darkgoldenrod','brown']
    for i in range(L):
        for j in range(L):
            nb = rd.randint(0,n)
            if nb>3: nb=4
            rect = canvas.create_rectangle((i*l_case,j*l_case), ((i+1)*l_case,(j+1)*l_case),
                        fill=liste_coul[nb])
            case = canvas.create_text((i*l_case+l_case//2,j*l_case+l_case//2), text=str(nb))
            grille[i][j] = case

def stabilisation():
    """focntion qui ne code uniquement la stabilisation (avalanche)
    pour ensuite creer une focntion qui ne code uniquement l'affichage sur la canvas de la configuration
    (Q: ne modifier que la grille et la renvoyer a la fin de la fonction ?)"""
    global grille, case, nb
    for i in range(L):
        for j in range(L):
            if canvas.itemconfigure('text')>3:
                nb-=1
                canvas.itemconfigure(grille[i][j], text=str(nb))
                canvas.itemconfigure(grille[i][j], text=str(nb)) #tentative de modifier nb des autres case lors de l'avalanche
    

def config_rd():
    """- creer une configuration aléatoire sur le canvas
    - se stabilise ensuite"""
    global grille, case, nb
    canvas.delete("all")
    liste_coul = ['lightgoldenrod','gold', 'goldenrod','darkgoldenrod']
    for i in range(L):
        for j in range(L):
            nb = rd.randint(0,5)
            rect = canvas.create_rectangle((i*l_case,j*l_case), ((i+1)*l_case,(j+1)*l_case),
                        fill=liste_coul[nb])
            case = canvas.create_text((i*l_case+l_case//2,j*l_case+l_case//2), text=str(nb))
            grille[i][j] = case
    canvas.after(2000, stabilisation)






# partie pricipale

# création widgets
racine = tk.Tk() # Création de la fenêtre racine
bouton = tk.Button(racine, text="initialisation", command=initialisation)
canvas = tk.Canvas(racine, height=HAUTEUR, width=LARGEUR, bd=10)
bouton_config = tk.Button(racine, text="configuration aléatoire", command=config_rd)



#placement des widgets
bouton.grid(column=0, row=1)
canvas.grid(column=0, row=0, columnspan=2)
bouton_config.grid(column=1, row=1)


#boucle principale
racine.mainloop()