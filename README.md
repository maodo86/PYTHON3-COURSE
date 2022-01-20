# PYTHON3-COURSE


## Exercices

<ins>Exercice 1</ins>  
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

<ins>Exercice 2</ins>  
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

<ins>Exercice 3</ins>  
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

<ins>Exercice 4</ins>  
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

<ins>Exercice 5</ins>  
* Définir la liste : liste =[17, 38, 10, 25, 72], puis effectuez les actions suivantes :
    * déterminer le minimun de cette liste
    * déterminer le maximum de cette liste
    * calculer la valeur moyenne de cette liste
    * déterminer les valeurs paires et impaires de cette liste et retouner dans deux tableaux pair et impaires les tuples renfermant a l'indexe 0 la valeur puis à l'indexe 1 le rang de cette valeur dans le tableau initial.

> Exemple: [1, 2, 3, 4] => pair = [(2, 1), (4, 3)], impair = [(1, 0), (3, 2)]

___

<ins>Exercice 6</ins>  
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

___

<ins>Exercice 7</ins>  
* Ecrire une application qui permet de renvoyer les indexes des lettres majuscules contenues dans la phrase "PythOn PouR LES Nuls"

> Exemple: ("HeLlO") ==> [0, 2, 4]

___

<ins>Exercice 8</ins>  
* Ecrire une application qui permet de renvoyer les indexes des lettres majuscules:
    * demander à l'utilisateur de donner une phrase ou un mot qui soit être une chaine de caractère:
        * veuillez à ce que la longueur de ce que l'utilisateur entre soit supérieure à 2 dans le cas contraire obnligez le à entrer la bonne phrase ou un mot dont la longueur est supérieur à 2
        * après retourner les indexes des lettres en majuscules
        * Puis tester l'application avec différentes phrases que voici:
            * HeLl0 ==> [0, 2, 4]
            * HeLlO Les etudiaNtS ==> [0, 2, 4, 6, 16, 18]

---

<ins>Exercice 9: Middle letter</ins>  
* Write a function named <code>mid</code> that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return "".  

---

<ins>Exercice 9: Online status</ins>  
* The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.
<br>
For example, consider the following dictionary:
```python3
statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
```

* In this case, the number of people online is 2.
* Write a function named <code>online_count</code> that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.
* Your function should return the number of people who are online.

---

<ins>Exercice 9: Randomness</ins>  
* Define a function, <code>random_number</code>, that takes no parameters. The function must generate a random integer between 1 and 100, both inclusive, and return it.
* Calling the function multiple times should (usually) return different numbers.
* For example, calling <code>random_number()</code> some times might first return 42, then 63, then 1.

---

<ins>Exercice 9: Adding and removing dots</ins>  
* Write a function named <code>add_dots</code> that takes a string and adds "." in between each letter. For example, calling <code>add_dots("test")</code> should return the string "t.e.s.t". Then, below the <code>add_dots</code> function, write another function named <code>remove_dots</code> that removes all dots from a string. For example, calling <code>remove_dots("t.e.s.t")</code> should return "test".
* If both functions are correct, calling <code>remove_dots(add_dots(string))</code> should return back the original string for any string.
* (You may assume that the input to add_dots does not itself contain any dots.)

---

<ins>Exercice 9: Counting syllables</ins>  
* Define a function named <code>count</code> that takes a single parameter. The parameter is a string. The string will contain a single word divided into syllables by hyphens, such as these:
"ho-tel"  
"cat"  
"met-a-phor"  
"ter-min-a-tor"  
* Your function should count the number of syllables and return it.  
* For example, the call <code>count("ho-tel")</code> should return 2.  

---

<ins>Exercice 10: Anagrams</ins>  
* Two strings are anagrams if you can make one from the other by rearranging the letters.  
Write a function named <code>is_anagram</code> that takes two strings as its parameters. Your function should return True if the strings are anagrams, and False otherwise.  
For example, the call <code>is_anagram("typhoon", "opython")</code> should return True while the call is_anagram("Alice", "Bob") should return False.

---

<ins>Exercice 10: Flatten a list</ins>  
* Write a function that takes a list of lists and flattens it into a one-dimensional list.
* Name your function <code>flatten</code>. It should take a single parameter and return a list.
For example, calling:
flatten([[1, 2], [3, 4]]) Should return the list: [1, 2, 3, 4]