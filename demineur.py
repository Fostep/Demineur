import random

# ------------------- FONCTIONS  -------------------

# Pose des bombes aleatoirement dans la matrice choisie
# pas de return, pas de print
def bombeAleatoire(matrice, chiffre):
  nbrBombe = 0
  while(nbrBombe < (chiffre*chiffre)//3):

    bombeLigne = random.randint(0,len(matrice)-1)
    bombeColonne = random.randint(0,len(matrice[0])-1)
    if(matrice[bombeLigne][bombeColonne] != 'b'):
      matrice[bombeLigne][bombeColonne] = 'b'
      chiffreCase(matrice, bombeLigne, bombeColonne)
      nbrBombe += 1 #nbrBombe = nbrBombe + 1

# Place +1 aux cases adjacentes d'une bombe
# pas de return, pas de print
def chiffreCase(matrice, ligneBombe, colonneBombe):
  #Regarde les 8 cases autour
  for i in range(ligneBombe-1, ligneBombe+2):
    for y in range(colonneBombe-1, colonneBombe+2):
      #Regarde si bien dans la matrice
      if i in range(0,len(matrice)):
        if y in range(0, len(matrice[0])):
          if matrice[i][y] != 'b':
            matrice[i][y] +=1

# Affiche la matrice choisie
# pas de return, print(matrice)
def Afficher(matrice, chiffre):
  #Affiche les numéros des colonnes
  print("   ",end="")
  for i in range(0, chiffre):
    print(i+1, end=" ")
  print("")
  #Affiche la ligne dessous
  print("  ",end="")
  print(chiffre*"--")
  #Affiche la matrice et le numéro des lignes
  for ligne in range(0,len(matrice)):
    print(ligne+1, end="| ")
    for colone in range(0,len(matrice[0])):
      print(matrice[ligne][colone], end=" ")
    print("")

# Creer les 2 matrices comportant les bombes et l'affichage
# return les 2 matrices, pas de print
def creerMatrice(chiffre):
  listeDem = []
  listeAff = []
  #Demineur
  for ligneDem in range(0, chiffre):
    listeDem.append([])
    for colonneDem in range(0,chiffre):
      listeDem[ligneDem].append(0)

  #Affichage
  for ligneAff in range(0, chiffre):
    listeAff.append([])
    for colonneAff in range(0,chiffre):
      listeAff[ligneAff].append('☐')
    
  return listeDem, listeAff

# Demande une ligne et une colonne dans le plateau
# return ligne, colonne, pas de print
def choixDeLaCase(taille):
  print("Quelle est votre ligne : ", end="") 
  ligne = int(input())-1
  while(ligne<0 or ligne>=taille):
    print("La ligne doit être comprise dans le plateau, ligne: ", end="") 
    ligne = int(input())-1
  
  print("Quelle est votre colonne : ", end="")
  colonne = int(input())-1
  while(colonne<0 or colonne>=taille):
    print("La colonne doit être comprise dans le plateau, colonne: ", end="") 
    colonne = int(input())-1
  return ligne, colonne

# Verifie si le joueur touche une bombe et maj matrice affichage
# pas de return, pas de print
def verifDefaite(matriceDem, matriceAff, ligne, colonne, nbr):
  if(matriceDem[ligne][colonne] != 'b'):
    if(matriceDem[ligne][colonne] == 0):

      matriceAff[ligne][colonne] = " "

      for ligneAut in range(ligne-1, ligne+2):
        for colonneAut in range(colonne-1,colonne+2):

          if ligneAut in range(0, len(matriceDem)):
            if colonneAut in range(0, len(matriceDem[0])):

              if(matriceDem[ligneAut][colonneAut] != 'b'):

                if(matriceDem[ligneAut][colonneAut] == 0):
                  matriceAff[ligneAut][colonneAut] = " "

                else:
                  matriceAff[ligneAut][colonneAut] = matriceDem[ligneAut][colonneAut]

                nbr = nbr-1
      return True, matriceDem, matriceAff, nbr

    else:
      print("-1 si chiffre")
      matriceAff[ligne][colonne] = matriceDem[ligne][colonne]
      return True, matriceDem, matriceAff, nbr-1
  else:
    matriceAff[ligne][colonne] = matriceDem[ligne][colonne]
    return False, matriceDem, matriceAff, nbr


  
# ------------------- MATRICE  ------------------- 
demineur = []
afficherDem = []

# ------------------- VARIABLES  ------------------- 
jouer = True
choixAction = 0
chiffresJoueur = 0
nbrCases = 0
nbrBombes = 0
nbrVictoire = 0
ligneJoueur = 0
colonneJoueur = 0
# ------------------- PRINCIPAL  ------------------- 
print("Combien boulez vous de lignes et de colonnes ?", end=" ")

#Demande de la taille de la matrice
chiffresJoueur = int(input())
while(chiffresJoueur <= 0):
  print("Incorrect, votre chiffre ne peux que être supérieur à 0.\nVeuillez le reprendre: ")
  chiffresJoueur = int(input())

# Calcul de la variable comptant les cases révélées
nbrCases = chiffresJoueur * chiffresJoueur
nbrBombes = (nbrCases)//3
nbrVictoire = nbrCases - nbrBombes

# Creation de la matrice
demineur, afficherDem = creerMatrice(chiffresJoueur)

# Affiche la matrice d'affichage
Afficher(afficherDem, chiffresJoueur) 

# Place les bombes
bombeAleatoire(demineur, chiffresJoueur) 
#Afficher(demineur, chiffresJoueur) #Affiche la matrice des infos

while(jouer == True and nbrVictoire != 0):
  # Demande au joueur ce qu'il veut faire
  print("Que souhaitez vous faire ?\n - Reveler une case : 1\n - Poser un drapeau : 2\n")
  choixAction = int(input())
  while(choixAction != 1 and choixAction !=2):
    print("Veuillez choisir une action :\n - Reveler une case : 1\n - Poser un drapeau : 2\n")
    choixAction = int(input())

  ligneJoueur, colonneJoueur = choixDeLaCase(chiffresJoueur) # Récupére la ligne du joueur
  if(choixAction == 1):
    jouer, demineur, afficherDem, nbrVictoire = verifDefaite(demineur, afficherDem, ligneJoueur, colonneJoueur, nbrVictoire)
    
  else:
    afficherDem[ligneJoueur][colonneJoueur] = '☒'
  Afficher(afficherDem, chiffresJoueur)


if(jouer == False):
  print("Vous avez perdu, vous ferez mieux la prochaine fois.")
else:
  print("Bravo vous avez gagné !")

#'☒'

