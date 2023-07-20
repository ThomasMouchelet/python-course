# Introduction au langage Python

## Introduction

Python est un langage de programmation interprété, c'est-à-dire qu'il n'est pas nécessaire de le compiler avant de l'exécuter. Il est multi-paradigme, c'est-à-dire qu'il permet de programmer selon plusieurs approches différentes. Il est orienté objet, c'est-à-dire qu'il permet de définir des classes et de créer des objets. Il est également fonctionnel, c'est-à-dire qu'il permet de définir des fonctions et de les utiliser comme des objets.


## Histoire

Python a été créé par Guido van Rossum en 1991. Le nom Python vient de la série télévisée Monty Python's Flying Circus. Python est un langage open source, c'est-à-dire que son code source est disponible publiquement. Python est un langage multiplateforme, c'est-à-dire qu'il peut être exécuté sur plusieurs systèmes d'exploitation différents.

## Utilisation

Python est un langage de programmation généraliste, c'est-à-dire qu'il peut être utilisé pour créer des applications de bureau, des applications web, des applications mobiles, des jeux vidéo, des scripts, etc. Python est également utilisé pour l'intelligence artificielle et le machine learning.

## Syntaxe

Python utilise une syntaxe simple et lisible. Il utilise l'indentation pour définir les blocs de code. Il utilise des espaces pour définir l'indentation. Il utilise des tabulations pour définir la séparation entre les éléments d'une instruction.

```python
# Exemple de syntaxe
if True:
    print("Hello World!")
```

## Interpréteur

Python utilise un interpréteur pour exécuter du code Python. L'interpréteur Python est un programme qui exécute du code Python. Il existe plusieurs interpréteurs Python. Le plus connu est l'interpréteur CPython. Il existe également l'interpréteur PyPy, l'interpréteur Jython, l'interpréteur IronPython, etc.

## Environnement de développement

Python peut être exécuté dans un environnement de développement. Il existe plusieurs environnements de développement pour Python. Le plus connu est l'environnement de développement IDLE. Il existe également l'environnement de développement PyCharm, l'environnement de développement Spyder, l'environnement de développement Visual Studio Code, etc.


## Installation

Pour installer Python, il suffit de télécharger le fichier d'installation sur le site officiel de Python (https://www.python.org/downloads/). Il est recommandé d'installer la dernière version de Python 3. Une fois le fichier téléchargé, il suffit de l'exécuter et de suivre les instructions.

Pour vérifier que Python est bien installé, il suffit d'ouvrir une invite de commande et de taper la commande suivante:

```bash
python --version
// or
python3 --version
```

Si Python est bien installé, la version de Python doit s'afficher.

Il également possible d'exécuter python avec une extension VScode. Pour cela, il suffit d'installer l'extension Python de Microsoft (https://marketplace.visualstudio.com/items?itemName=ms-python.python). Une fois l'extension installée, il est possible d'exécuter du code Python directement dans VScode.

## Exécution d'un script Python

Pour exécuter un script Python, il suffit d'ouvrir une invite de commande et de taper la commande suivante:

```bash
python3 script.py
```

## Exécution interactive

Python permet d'exécuter des instructions de manière interactive. Pour cela, il suffit d'ouvrir une invite de commande et de taper la commande suivante:

```bash
python3
```

Une fois dans l'interpréteur Python, il est possible d'exécuter des instructions Python. Pour quitter l'interpréteur Python, il suffit de taper la commande suivante:

```bash
exit()
```

## Documentation

La documentation officielle de Python est disponible à l'adresse suivante: https://docs.python.org/3/

## Exercices

### Exercice 1

Écrire un script Python qui affiche le message suivant:

```
Hello World!
```

## Affichage

Python permet d'afficher des messages à l'écran. Pour cela, il suffit d'utiliser la fonction `print()`.

```python
print("Hello World!")
```

## Variables

Python permet de définir des variables. Pour cela, il suffit d'utiliser le symbole `=`.

```python
message = "Hello World!"
print(message)
```

Le symbole `=` est un opérateur d'assignation. Il permet d'assigner une valeur à une variable.
Il également possible de réassigner une valeur à une variable.

```python
message = "Hello World!"
print(message)
message = "Hello World Again!"
print(message)
```

### Assignation multiple

Python permet de définir plusieurs variables en même temps. Pour cela, il suffit d'utiliser le symbole `,`.

```python
message1, message2 = "Hello", "World!"
print(message1)
print(message2)
```

### Nom de variables

Python permet de définir des variables avec des noms de variables composés de lettres, de chiffres et du caractère `_`. Les noms de variables ne peuvent pas commencer par un chiffre.

```python
message = "Hello World!"
print(message)
```

### Noms de variables réservés

Python permet de définir des variables avec des noms de variables réservés. Les noms de variables réservés ne peuvent pas être utilisés comme nom de variable.

```python
# Exemple de noms de variables réservés
and = "Hello World!"
print(and)
```

### Noms de variables en majuscules

Python permet de définir des variables avec des noms de variables en majuscules. Les noms de variables en majuscules sont généralement utilisés pour définir des constantes.

```python
# Exemple de noms de variables en majuscules
MESSAGE = "Hello World!"
print(MESSAGE)
```

## Commentaires

Python permet d'ajouter des commentaires. Pour cela, il suffit d'utiliser le symbole `#`.

```python
# Ceci est un commentaire
```

## Concaténation

Python permet de concaténer des chaînes de caractères. Pour cela, il suffit d'utiliser le symbole `+`.

```python
message = "Hello" + " " + "World!"
print(message)
```

## Types de données

Python permet de définir plusieurs types de données. Les types de données les plus courants sont les suivants:

- `int`: entier
- `float`: nombre à virgule flottante
- `str`: chaîne de caractères
- `bool`: booléen

## Changement de type

Python permet de changer le type d'une variable. Pour cela, il suffit d'utiliser les fonctions suivantes:

- `int()`: convertit une valeur en entier
- `float()`: convertit une valeur en nombre à virgule flottante
- `str()`: convertit une valeur en chaîne de caractères
- `bool()`: convertit une valeur en booléen

```python
# Exemple de changement de type
message = "Hello World!"
print(message)
print(type(message))
message = 42
print(message)
print(type(message))
message = str(message)
print(message)
print(type(message))
```

## Opérateurs

Python permet d'utiliser plusieurs opérateurs. Les opérateurs les plus courants sont les suivants:

- `+`: addition
- `-`: soustraction
- `*`: multiplication
- `/`: division
- `//`: division entière
- `%`: modulo
- `**`: puissance

## Entrée utilisateur

Python permet de demander une entrée utilisateur. Pour cela, il suffit d'utiliser la fonction `input()`. Cette fonction renvoie une chaîne de caractères. Dans l'exemple suivant, la fonction `input()` est utilisée pour demander une entrée utilisateur et la fonction `print()` est utilisée pour afficher l'entrée utilisateur.

```python
message = input("Entrez un message: ")
print(message)
```

## Ateliers

### Atelier 1

Écrire un script Python qui demande à l'utilisateur son nom et qui affiche le message suivant:

```
Hello <nom> !
```

### Atelier 2

Écrire un script Python qui demande à l'utilisateur son nom et son âge et qui affiche le message suivant:

```
Hello <nom> ! Vous avez <age> ans.
```

### Atelier 3

Écrire un script Python qui demande à l'utilisateur son nom et son âge et qui affiche le message suivant:

```
Hello <nom> ! Vous avez <age> ans. Dans 10 ans, vous aurez <age + 10> ans.
```
