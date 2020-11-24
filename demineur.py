from random import randint

# -------------------------------- FONCTIONS --------------------------------
#Ajoute aléatoirement les bombes dans la matrice
#Renvoie la matrice
def AleaBombe(list):
  incr = 0
  while(incr<20):
    ligne = randint(0,8)
    colonne = randint(0,8)

    if(list[ligne][colonne] != 'b'):
      list[ligne][colonne] = 'b'
      incr += 1
      list = ajoutCaseAdj(list, ligne, colonne)
  return list

#Vérifie que l'on peut augmenter de +1 les cases autour de la mise en place de la bombe
#Renvoie la matrice
def ajoutCaseAdj(liste, ligB, colB):
  if (ligB-1>=0 and colB-1>=0):
    if(liste[ligB-1][colB-1] != 'b'):
      liste[ligB-1][colB-1] = liste[ligB-1][colB-1]+1

  if(ligB-1>=0):
    if(liste[ligB-1][colB] != 'b'):
      liste[ligB-1][colB] = liste[ligB-1][colB]+1

  if(ligB-1>=0 and colB+1<9):
    if(liste[ligB-1][colB+1] != 'b'):
      liste[ligB-1][colB+1] = liste[ligB-1][colB+1]+1

  if(colB-1>=0):
    if(liste[ligB][colB-1] != 'b'):
      liste[ligB][colB-1] = liste[ligB][colB-1]+1

  if(colB+1<0):
    if(liste[ligB][colB+1] != 'b'):
      liste[ligB][colB+1] = liste[ligB][colB+1]+1

  if(ligB+1<9 and colB-1>=0):
    if(liste[ligB+1][colB-1] != 'b'):
      liste[ligB+1][colB-1] = liste[ligB+1][colB-1]+1

  if(ligB+1<9):
    if(liste[ligB+1][colB] != 'b'):
      liste[ligB+1][colB] = liste[ligB+1][colB]+1

  if(ligB+1<9 and colB+1<9):
    if(liste[ligB+1][colB+1] != 'b'):
      liste[ligB+1][colB+1] = liste[ligB+1][colB+1]+1
  
  return liste

#Affiche la liste servant à afficher
#Renvoie rien
def AfficherMatrice(list):
  print("   1 2 3 4 5 6 7 8 9")
  print("  ------------------")
  for i in range(0,9):
    print(i+1, end="")
    print("|", end="")
    for y in range(0,9):
      print(" ", end="")
      print(list[i][y], end="")
    print("")

#Choix de la ligne et colonne, boucle si incorrect.
#Renvoie ligne et colonne
def ChoixJoueur():
  print("Choix ligne: ", end="")
  ligne= int(input())

  while(ligne-1<0 and ligne-1>8):
    print("Ligne incorrect, veuillez en choisir une autre: ", end="")
    ligne= int(input())
  
  print("Choix colonne: ", end="")
  colonne= int(input())

  while(colonne-1<0 and colonne-1>8):
    print("Colonne incorrect, veuillez en choisir une autre: ", end="")
    colonne= int(input())

  return ligne, colonne

#Affiche la case choisie par le joueur
#Renvoie bool pour partie
def AppliqueChoix(liste,matr, ligneJ, colonneJ):
  liste[ligneJ][colonneJ] = matr[ligneJ][colonneJ]
  AfficherMatrice(liste)
  if(matr[ligneJ][colonneJ]=='b'):
    return False
  else:
    return True
# -------------------------------- Variables et autres --------------------------------
matrice = [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]

afficher = [['□','□','□','□','□','□','□','□','□'],['□','□','□','□','□','□','□','□','□'],['□','□','□','□','□','□','□','□','□'],['□','□','□','□','□','□','□','□','□'],['□','□','□','□','□','□','□','□','□'],['□','□','□','□','□','□','□','□','□'],['□','□','□','□','□','□','□','□','□'],['□','□','□','□','□','□','□','□','□'],['□','□','□','□','□','□','□','□','□']]

ligneJoueur = -1
colonneJoueur = -1
partie = True
# -------------------------------- Initialisation --------------------------------
matrice = AleaBombe(matrice)
AfficherMatrice(afficher)
AfficherMatrice(matrice)
print("\nJeu du démineur:")
while(partie):
  #ligne colonne a jouer
  ligneJoueur, colonnejoueur = ChoixJoueur()
  partie = AppliqueChoix(afficher, matrice, ligneJoueur-1, colonnejoueur-1)

print("DEFAITE")
