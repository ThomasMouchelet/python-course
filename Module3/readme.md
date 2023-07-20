## Les boucles

Les boucles permettent de répéter une ou plusieurs instructions. Il existe deux types de boucles:

- La boucle `for`
- La boucle `while`

### La boucle `for`

La boucle `for` permet de répéter une ou plusieurs instructions pour chaque élément d'une liste.

```python
# Exemple de boucle for
for i in [1, 2, 3]:
    print(i)
```

### La boucle `while`

La boucle `while` permet de répéter une ou plusieurs instructions tant qu'une condition est vérifiée.

```python
# Exemple de boucle while
i = 0
while i < 3:
    print(i)
    i = i + 1
```

### Atelier 1

Écrire un script Python qui affiche les nombres de 1 à 10.

### Atelier 2

Écrire un script Python qui demande un mot de passe à l'utilisateur. Si le mot de passe est incorrect, le script doit redemander un mot de passe à l'utilisateur. Si le mot de passe est correct, le script doit afficher le message suivant:

```
Mot de passe correct.
```

## Les modules

Les modules permettent d'ajouter des fonctionnalités à Python. Pour utiliser un module, il faut l'importer. Pour cela, il suffit d'utiliser le mot-clé `import` suivi du nom du module.

```python
# Exemple d'importation de module
import math
```

```python
# Exemple d'utilisation de module
import random
print(random.randint(1, 10))
```

```python
# Exemple d'utilisation de module
import datetime
print(datetime.datetime.now())
```

### Atelier 3

Écrire un script Python qui affiche la date et l'heure actuelle.

### Atelier 4

Écrire un script Python qui demande à l'utilisateur un nombre entre 1 et 10. Si le nombre est incorrect, le joueur a perdu. Si le nombre est correct, le joueur a gagné.

### Atelier 5

Écrire un script Python qui demande à l'utilisateur un nombre entre 1 et 10. Si le nombre est incorrect, le script doit redemander un nombre à l'utilisateur. Si le nombre est correct, le script doit afficher le message suivant:

```
Nombre correct.
```

### Atelier 6

Écrire un script Python qui demande à l'utilisateur un nombre entre 1 et 10. Si le nombre est incorrect, le script doit redemander un nombre à l'utilisateur. L'utilisateur est limité à 3 tentatives. Si l'utilisateur n'a pas trouvé le nombre au bout de 3 tentatives, le joueur a perdu. Si le nombre est correct, le script doit afficher le message suivant:

```
Nombre correct.
```