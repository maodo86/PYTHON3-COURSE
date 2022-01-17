# PYTHON3-COURSE


## Exercices

* Affectez les variables temps et distance par les valeurs 6.892 (s) et 19.7(m)  
    * Calculez et affichez la valeur de la vitesse.  
    * Améliorez l’affichage en imposant un chiffre après le point décimal.  
    * Affichez les résultats de cette vitesse dans différentes unités de mesure à savoir:
        * le m/s
        * le m/ms
        * le km/s
        * le km/ms
```python3
# Pour le formatage de l'affichage voici des exemples à appliquer. 

# affichage formate :
print("{}".format("-"*23))
print("\n vitesse = {:.2f} m/s".format(vitesse)) # arrondi a 2 chiffres
```

___

* Affectez les variables poids et taille par les valeurs 196 (kg) et 1.75 (m) 
    * Calculez l'indice de masse corporelle de cet individu  
    * Améliorez l’affichage en imposant un chiffre après le point décimal.  
    * Puis déterrminer dans quelle catégorie il est:
        * IMC entre 30 et 34,9 : classe I (obésité modérée)  
        * IMC entre 35-39,9 : classe II (obésité sévère)  
        * IMC ≥ 40 kg/m² : classe III (obésité massive ou morbide)  
```python3
# Pour le formatage de l'affichage voici des exemples à appliquer. 

# affichage formate :
print("{}".format("-"*23))
print("\n vitesse = {:.2f} m/s".format(vitesse)) # arrondi a 2 chiffres
```

___

* Reprenez l'exercice 1 en prenant le soin cette fois ci de demander à l'utilisateur de renseigner les informations par rapport à la vitesse et par rapport à la distance:
    * Ecriver l'algorithme qui sera implémenté (syntaxe algorithme):
        * Demander à l'utilisateur de renseigner un nombre entier supérieur à 10 pour le temps. Tant que la condition n'est pas respectée répéter l'instruction jusquà ce qu'il donne la bonne valeur
        * Demander lui de renseigner la distance qui soit positive et supérieur à 28.8. Tant que ces conditions ne sont pas respectées redemander le jusquà obtention de la bonne distance
        * Convertisser le résultat de la vitesse en:
            * m/s
            * m/ms
            * km/s
            * km/ms
    * Implémenter en fonction de l'algorithme de manière stricte le code python qui va avec.

> Veuillez à toujours nommé vos variables avec des noms explicites. Exemple: temps, distance ou encore poids ou taille comme nom de variable.

> Pour demander à la console à l'utilisateur utiliser la fonction <code>input()</code>. Comme exemple le code suivant:

```python3
nom = str(input('Entrer vôtre nom: '))
age = int(input('Entrer vôtre age: '))
sex = str(input('Entrer vôtre sex: '))
sal = float(input('Entrer vôtre salaire: '))
```

___

* Reprenez l'exercice 2 en prenant le soin cette fois ci de demander à l'utilisateur de renseigner les informations par rapport à son poids et par rapport à sa taille:
    * Ecriver l'algorithme qui sera implémenté (syntaxe algorithme):
        * Demander à l'utilisateur de renseigner un nombre entier concernant son poids. Tant que la condition n'est pas respectée répéter l'instruction jusquà ce qu'il donne la bonne valeur
        * Demander lui de renseigner sa taille qui doit être strictement positif sinon qu'il reprenne l'instruction autant de fois qu'il faudra.
    * Implémenter en fonction de l'algorithme de manière stricte le code python qui va avec.

> Veuillez à toujours nommé vos variables avec des noms explicites. Exemple: temps, distance ou encore poids ou taille comme nom de variable.

> Pour demander à la console à l'utilisateur utiliser la fonction <code>input()</code>. Comme exemple le code suivant:

```python3
nom = str(input('Entrer vôtre nom: '))
age = int(input('Entrer vôtre age: '))
sex = str(input('Entrer vôtre sex: '))
sal = float(input('Entrer vôtre salaire: '))
```

___

* Définir la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :
    * déterminer le minimun de cette liste
    * déterminer le maximum de cette liste
    * calculer la valeur moyenne de cette liste
    * déterminer les valeurs paires et impaires de cette liste et retouner dans deux tableaux pair et impaires les tuples renfermant a l'indexe 0 la valeur puis à l'indexe 1 le rang de cette valeur dans le tableau initial.

> Exemple: [1, 2, 3, 4] => pair = [(2, 1), (4, 3)], impair = [(1, 0), (3, 2)]

___

* Définir la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :
    * triez et affichez la liste;
    * ajoutez l’élément 12 à la liste et affichez la liste;
    * renversez et affichez la liste;
    * affichez l’indice de l’élément 17;
    * enlevez l’élément 38 et affichez la liste;
    * affichez la sous-liste du 2e au 3e élément;
    * affichez la sous-liste du début au 2e élément;
    * affichez la sous-liste du 3e élément à la fin de la liste;
    * affichez la sous-liste complète de la liste;

