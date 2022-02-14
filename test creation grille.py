grille = []
for i in range(L):
    for j in range(L):
            grille.append([i,j])
print(grille)


for i in range(L):
    for j in range(L):
        nb = rd.randint(0,3)
        case = tk.Label(racine, text=str(nb))
        case.grid(column=i, row=j)
