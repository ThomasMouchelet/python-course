## Les listes

Les tableaux permettent de stocker plusieurs valeurs dans une seule variable. Pour créer un tableau, il suffit d'utiliser les crochets `[]`.

```python
# Exemple de tableau
nombres = [1, 2, 3]
print(nombres)
```

Il est possible d'accéder à un élément du tableau en utilisant son index. L'index d'un tableau commence à 0.

```python
# Exemple d'accès à un élément du tableau
nombres = [1, 2, 3]
print(nombres[0])
print(nombres[1])
print(nombres[2])
```

Il est possible de modifier un élément du tableau en utilisant son index.

```python
# Exemple de modification d'un élément du tableau
nombres = [1, 2, 3]
nombres[0] = 4
print(nombres)
```

Il est possible de supprimer un élément du tableau en utilisant son index.

```python
# Exemple de suppression d'un élément du tableau
nombres = [1, 2, 3]
del nombres[0]
print(nombres)
```

Il est possible de supprimer un élément du tableau en utilisant sa valeur.

```python
# Exemple de suppression d'un élément du tableau
nombres = [1, 2, 3]
nombres.remove(1)
print(nombres)
```

Il est possible de supprimer tous les éléments du tableau.

```python
# Exemple de suppression de tous les éléments du tableau

nombres = [1, 2, 3]
nombres.clear()
print(nombres)
```

Il est possible de connaître le nombre d'éléments du tableau.

```python
# Exemple de nombre d'éléments du tableau
nombres = [1, 2, 3]
print(len(nombres))
```

Il est possible de connaître l'index d'un élément du tableau.

```python
# Exemple de l'index d'un élément du tableau
nombres = [1, 2, 3]
print(nombres.index(2))
```

Il est possible de connaître le nombre d'occurrences d'un élément du tableau.

```python
# Exemple du nombre d'occurrences d'un élément du tableau
nombres = [1, 2, 3, 2]
print(nombres.count(2))
```

Il est possible de trier les éléments du tableau.

```python
# Exemple de tri des éléments du tableau
nombres = [3, 2, 1]
nombres.sort()
print(nombres)
```

Il est possible de trier les éléments du tableau dans l'ordre inverse.

```python
# Exemple de tri des éléments du tableau dans l'ordre inverse
nombres = [1, 2, 3]
nombres.sort(reverse=True)
print(nombres)
```

Il est possible de copier un tableau.

```python
# Exemple de copie d'un tableau
nombres = [1, 2, 3]
nombres_copie = nombres.copy()
print(nombres_copie)
```

Il est possible de fusionner deux tableaux.

```python
# Exemple de fusion de deux tableaux
nombres1 = [1, 2, 3]
nombres2 = [4, 5, 6]
nombres = nombres1 + nombres2
print(nombres)
```

Il est possible de fusionner deux tableaux.

```python
# Exemple de fusion de deux tableaux
nombres1 = [1, 2, 3]
nombres2 = [4, 5, 6]
nombres1.extend(nombres2)

print(nombres1)
```

Il est possible de créer un tableau avec des valeurs par défaut.

```python
# Exemple de création d'un tableau avec des valeurs par défaut
nombres = [0] * 3
print(nombres)
```

### Atelier 1

Écrire un script Python qui demande à l'utilisateur d'entrer 5 nombres. Le script doit ensuite afficher le plus grand nombre.

### Atelier 2

Écrire un script Python qui permet à l'utilisateur de renseigner plusieurs nombres. Le script doit ensuite afficher la moyenne des nombres.

### Atelier 3

Pierre feuille ciseaux est un jeu à deux joueurs. Chaque joueur choisit entre pierre, feuille et ciseaux. Les règles sont les suivantes:

- La pierre bat les ciseaux
- Les ciseaux battent la feuille
- La feuille bat la pierre

Écrire un script Python qui demande à l'utilisateur de choisir entre pierre, feuille et ciseaux. Le script doit ensuite choisir aléatoirement entre pierre, feuille et ciseaux. Le script doit ensuite afficher le choix de l'utilisateur et le choix du script. Le script doit ensuite afficher le résultat de la partie.

## Tableaux multidimensionnels

Les tableaux multidimensionnels permettent de stocker plusieurs valeurs dans une seule variable. Pour créer un tableau multidimensionnel, il suffit d'utiliser les crochets `[]`.

```python
# Exemple de tableau multidimensionnel
nombres = [[1, 2, 3], [4, 5, 6]]
print(nombres)
```

Il est possible d'accéder à un élément du tableau multidimensionnel en utilisant son index. L'index d'un tableau commence à 0.

```python
# Exemple d'accès à un élément du tableau multidimensionnel
nombres = [[1, 2, 3], [4, 5, 6]]
print(nombres[0][0])
print(nombres[0][1])
print(nombres[0][2])
print(nombres[1][0])
print(nombres[1][1])
print(nombres[1][2])
```

## Dictionnaires

Les dictionnaires permettent de stocker plusieurs valeurs dans une seule variable. Pour créer un dictionnaire, il suffit d'utiliser les accolades `{}`.

```python
# Exemple de dictionnaire
personne = {
    "nom": "Jean",
    "age": 20
}

print(personne)
```

Il est possible d'accéder à une valeur du dictionnaire en utilisant sa clé.

```python
# Exemple d'accès à une valeur du dictionnaire
personne = {
    "nom": "Jean",
    "age": 20
}

print(personne["nom"])
print(personne["age"])
```

Il est possible de modifier une valeur du dictionnaire en utilisant sa clé.

```python
# Exemple de modification d'une valeur du dictionnaire
personne = {
    "nom": "Jean",
    "age": 20
}

personne["nom"] = "Pierre"
print(personne)
```

Il est possible de supprimer une valeur du dictionnaire en utilisant sa clé.

```python
# Exemple de suppression d'une valeur du dictionnaire
personne = {
    "nom": "Jean",
    "age": 20
}

del personne["nom"]
print(personne)
```

Il est possible de supprimer toutes les valeurs du dictionnaire.

```python
# Exemple de suppression de toutes les valeurs du dictionnaire
personne = {
    "nom": "Jean",
    "age": 20
}

personne.clear()
print(personne)
```

Il est possible de connaître le nombre de valeurs du dictionnaire.

```python
# Exemple du nombre de valeurs du dictionnaire
personne = {
    "nom": "Jean",
    "age": 20
}

print(len(personne))
```

Il est possible de connaître les clés du dictionnaire.

```python
# Exemple des clés du dictionnaire
personne = {
    "nom": "Jean",
    "age": 20
}

print(personne.keys())
```

Il est possible de connaître les valeurs du dictionnaire.

```python
# Exemple des valeurs du dictionnaire
personne = {
    "nom": "Jean",
    "age": 20
}

print(personne.values())
```

Il est possible de connaître les clés et les valeurs du dictionnaire.

```python
# Exemple des clés et des valeurs du dictionnaire
personne = {
    "nom": "Jean",
    "age": 20
}

print(personne.items())
```


## Ateliers

```python
users = [
    {
        "id": 1,
        "name": 'John',
        "age": 25,
    },
    {
        "id": 2,
        "name": 'Jane',
        "age": 22,
    },
    {
        "id": 3,
        "name": 'Bill',
        "age": 32,
    },
    {
        "id": 4,
        "name": 'Mary',
        "age": 27,
    },
    {
        "id": 5,
        "name": 'Jack',
        "age": 21,
    },
    {
        "id": 6,
        "name": 'Jill',
        "age": 19,
    },
    {
        "id": 7,
        "name": 'Joe',
        "age": 23,
    },
    {
        "id": 8,
        "name": 'Jen',
        "age": 26,
    },
    {
        "id": 6,
        "name": 'Jill',
        "age": 19,
    },
]
```

### Atelier 4

Écrire une fonction qui retourne la somme de tous les âges.

### Atelier 5

Écrire une fonction qui retourne le nom de l'utilisateur le plus âgé.

### Atelier 6

Écrire une fonction qui forme de manière aléatoire des couples d'utilisateurs. Chaque utilisateur doit être présent dans un seul couple. Chaque couple doit être unique. La fonction doit retourner une liste de couples.

## Mutabilité

Les types de données suivants sont mutables:

- list
- dict
- set

Les types de données suivants sont immutables:

- int
- float
- bool
- str
- tuple


```python
prenom = "Thomas"
prenom = "Sophie"
print(prenom)
```

On ne modifie pas la chaîne de caractères "Thomas". On réassigne la variable prenom à une nouvelle chaîne de caractères "Sophie". La chaîne "Thomas" reste immuable.

```python
ma_liste = [1, 2, 3]
ma_liste[0] = 10
print(ma_liste)
```

Ici, on modifie réellement le premier élément de la liste. La liste a été modifiée sur place, c'est pour cela qu'on dit que les listes sont mutables.

Les chaînes de caractères sont immuables car on ne peux pas modifier un caractère individuel dans la chaîne sans créer une nouvelle chaîne. Les listes sont mutables on peux modifier, ajouter ou supprimer des éléments dans une liste après sa création.


## Les tuples

La principale différence entre les listes et les tuples est que les listes sont modifiables (ou "mutables"), ce qui signifie que vous pouvez changer leurs éléments après leur création. En revanche, les tuples sont immuables, ce qui signifie que vous ne pouvez pas changer leurs éléments une fois qu'ils ont été créés.

Les tuples permettent de stocker plusieurs valeurs dans une seule variable. Pour créer un tuple, il suffit d'utiliser les parenthèses `()`.

```python
# Exemple de tuple
nombres = (1, 2, 3)
print(nombres)
```

Il est possible d'accéder à un élément du tuple en utilisant son index. L'index d'un tuple commence à 0.

```python
# Exemple d'accès à un élément du tuple
nombres = (1, 2, 3)
print(nombres[0])
print(nombres[1])
print(nombres[2])
```

Il est possible de modifier un élément du tuple en utilisant son index.

```python
# Exemple de modification d'un élément du tuple
nombres = (1, 2, 3)
nombres[0] = 4
print(nombres)
```

Il est possible de supprimer un élément du tuple en utilisant son index.

```python
# Exemple de suppression d'un élément du tuple
nombres = (1, 2, 3)
del nombres[0]
print(nombres)
```

Il est possible de supprimer un élément du tuple en utilisant sa valeur.

```python
# Exemple de suppression d'un élément du tuple
nombres = (1, 2, 3)
nombres.remove(1)
print(nombres)
```

Il est possible de supprimer tous les éléments du tuple.

```python
# Exemple de suppression de tous les éléments du tuple

nombres = (1, 2, 3)
nombres.clear()
print(nombres)
```

Il est possible de connaître le nombre d'éléments du tuple.

```python
# Exemple de nombre d'éléments du tuple
nombres = (1, 2, 3)
print(len(nombres))
```

Il est possible de connaître l'index d'un élément du tuple.

```python
# Exemple de l'index d'un élément du tuple
nombres = (1, 2, 3)
print(nombres.index(2))
```

