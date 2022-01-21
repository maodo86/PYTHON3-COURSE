# Lecture / Ecriture dans les fichiers (Part 2)

def jumpNextLine():
    print('\n')


# def writeFile(filename: str):
#     file = open(filename,"w")

#     file.write("Salut tout le monde")
#     file.write("This is our new text file")
#     file.write("and this is another line.")
#     file.write("Why? Because we can.")

#     file.close()


# def writeFile(filename: str):
#     with open(filename,"w") as file:
#         file.write("Hello World")
#         file.write("This is our new text file")
#         file.write("and this is another line.")
#         file.write("Why? Because we can.")

#         file.close()


# (Exo):
# Lis le contenu du fichier file1.
# Nettoyer les caractère indésirables comme suit:
# Remplacer les '.' par des ''
# Remplacer les '!' par des ''
# Remplacer les '?' par des ''
# Remplacer les '\n' par des ' '
# Puis transforme le contenu en tableau
# Puis trie le tableau en ordre alphabetique
# Puis dans ce tableau tranformer chaque item avec un tuple
# Ce tuple doit contenir en Index O le numéro du mot
# Ce tuple foit contenir en Index 1 la valeur de l'item
# Ensuite ecriver dans un nouveau fichier du nom de extract.txt:
# Ecriver chaque item a chaque line comme suit:
# (Valeur1 : Numero)
# (Valeur2 : Numero)
# (Valeur3 : Numero)
# Veuillez à ce que aux items multiple de 10 (10 - 20 - 30 ...):
# que vous ajouter une line contenant des tirets de 6 à une longeur égale au mutilple de 10:
# Exemple (avec un multiple de 3):
# (Valeur1 : Numero)
# (Valeur2 : Numero)
# (Valeur3 : Numero)
# ---
# (Valeur4 : Numero)
# (Valeur5 : Numero)
# (Valeur6 : Numero)
# ------
# (Valeur7 : Numero)
# (Valeur8 : Numero)
# (Valeur9 : Numero)
# ---------


if __name__ == '__main__':
    writeFile('files/file1.txt')
