## Opérateurs de comparaison

Les opérateurs de comparaison permettent de comparer deux valeurs. Les opérateurs de comparaison les plus courants sont les suivants:

- `==`: égal à
- `!=`: différent de
- `>`: supérieur à
- `<`: inférieur à
- `>=`: supérieur ou égal à
- `<=`: inférieur ou égal à

### Exemple

```python
# Exemple d'opérateurs de comparaison
print(1 == 1)
print(1 != 1)
print(1 > 1)
print(1 < 1)
print(1 >= 1)
print(1 <= 1)
```

## Opérateurs logiques

Les opérateurs logiques permettent de combiner plusieurs conditions. Les opérateurs logiques les plus courants sont les suivants:

- `and`: et
- `or`: ou
- `not`: non

Avec l'opérateur `and`, la condition est vérifiée si toutes les conditions sont vérifiées.

```python
# Exemple d'opérateur and
print(True and True) # true
print(True and False) # false
print(False and True) # false
print(False and False) # false
```

Avec l'opérateur `or`, la condition est vérifiée si au moins une condition est vérifiée.

```python
# Exemple d'opérateur or
print(True or True) # true
print(True or False) # true
print(False or True) # true
print(False or False) # false
```

### Exemple

```python
# Exemple d'opérateurs logiques
print(True and True)
print(True and False)
print(True or True)
print(True or False)
print(not True)
```

## Les conditions

Les conditions permettent d'exécuter un bloc de code si une condition est vérifiée. Pour cela, il suffit d'utiliser le mot-clé `if` suivi de la condition et du symbole `:`. Le bloc de code à exécuter doit être indenté.

```python
if 1 == 1:
    print("1 est égal à 1")
```

Il est possible d'ajouter un bloc de code à exécuter si la condition n'est pas vérifiée. Pour cela, il suffit d'utiliser le mot-clé `else` suivi du symbole `:`. Le bloc de code à exécuter doit être indenté.

```python
if 1 == 2:
    print("1 est égal à 2")
else:
    print("1 n'est pas égal à 2")
```

Il est possible d'ajouter plusieurs conditions. Pour cela, il suffit d'utiliser le mot-clé `elif` suivi de la condition et du symbole `:`. Le bloc de code à exécuter doit être indenté.

```python
if 1 == 2:
    print("1 est égal à 2")
elif 1 == 3:
    print("1 est égal à 3")
else:
    print("1 n'est pas égal à 2 ni à 3")
```

## Ateliers

### Atelier 1

Écrire un script Python qui demande à l'utilisateur son age et qui affiche le message suivant:

```python
Vous êtes majeur.
# ou
Vous êtes mineur.
```

### Atelier 2

Écrire un script Python qui demande à l'utilisateur son age et qui indiquer à quel carte de fidélité il a droit:

- moins de 12 ans: carte enfant
- entre 12 et 18 ans: carte jeune
- entre 18 et 27 ans: carte jeune
- plus de 27 ans: carte sénior
