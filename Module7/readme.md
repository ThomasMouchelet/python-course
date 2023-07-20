## Les fichiers

### Introduction

Les fichiers sont des objets qui permettent de stocker des données sur le disque dur de l'ordinateur. Il existe deux types de fichiers : les fichiers textes et les fichiers binaires. Les fichiers textes sont des fichiers qui contiennent du texte. Les fichiers binaires sont des fichiers qui contiennent des données binaires (des données qui ne sont pas du texte).

### Ouverture d'un fichier

Pour ouvrir un fichier, il suffit d'utiliser la fonction `open`. Cette fonction prend deux paramètres : le chemin du fichier et le mode d'ouverture. Le chemin du fichier est une chaîne de caractères qui indique l'emplacement du fichier sur le disque dur. Le mode d'ouverture est une chaîne de caractères qui indique si le fichier doit être ouvert en lecture, en écriture ou en lecture et écriture. Pour ouvrir un fichier en lecture, il faut utiliser le mode `"r"`. Pour ouvrir un fichier en écriture, il faut utiliser le mode `"w"`. Pour ouvrir un fichier en lecture et écriture, il faut utiliser le mode `"r+"`.

```python
# Exemple d'ouverture d'un fichier
fichier = open("fichier.txt", "r")
```

### Fermeture d'un fichier

Pour fermer un fichier, il suffit d'utiliser la méthode `close`.

```python
# Exemple de fermeture d'un fichier
fichier = open("fichier.txt", "r")
fichier.close()
```

### Lecture d'un fichier

Pour lire le contenu d'un fichier, il suffit d'utiliser la méthode `read`. Cette méthode retourne une chaîne de caractères qui contient le contenu du fichier.

```python
# Exemple de lecture d'un fichier
fichier = open("fichier.txt", "r")
contenu = fichier.read()
print(contenu)
fichier.close()
```

### Écriture dans un fichier

Pour écrire dans un fichier, il suffit d'utiliser la méthode `write`. Cette méthode prend une chaîne de caractères en paramètre et écrit cette chaîne de caractères dans le fichier.

```python
# Exemple d'écriture dans un fichier
fichier = open("fichier.txt", "w")
fichier.write("Bonjour, je m'appelle Jean.")
fichier.close()
```

### Ajout de contenu dans un fichier

Pour ajouter du contenu dans un fichier, il suffit d'utiliser la méthode `write` avec le mode `"a"`. Cette méthode prend une chaîne de caractères en paramètre et ajoute cette chaîne de caractères à la fin du fichier.

```python
# Exemple d'ajout de contenu dans un fichier
fichier = open("fichier.txt", "a")
fichier.write("Bonjour, je m'appelle Jean.")
fichier.close()
```

### Parcourir un fichier ligne par ligne

Pour parcourir un fichier ligne par ligne, il suffit d'utiliser une boucle `for` avec la méthode `readlines`. Cette méthode retourne une liste de chaînes de caractères qui contient les lignes du fichier.

```python
# Exemple de parcours d'un fichier ligne par ligne
fichier = open("fichier.txt", "r")
lignes = fichier.readlines()
for ligne in lignes:
    print(ligne)
fichier.close()
```

### Parcourir un fichier caractère par caractère

Pour parcourir un fichier caractère par caractère, il suffit d'utiliser une boucle `for` avec la méthode `read`. Cette méthode retourne une chaîne de caractères qui contient le contenu du fichier.

```python

# Exemple de parcours d'un fichier caractère par caractère
fichier = open("fichier.txt", "r")
contenu = fichier.read()
for caractere in contenu:
    print(caractere)
fichier.close()
```

### Parcourir un fichier mot par mot

Pour parcourir un fichier mot par mot, il suffit d'utiliser une boucle `for` avec la méthode `read`. Cette méthode retourne une chaîne de caractères qui contient le contenu du fichier.

```python
# Exemple de parcours d'un fichier mot par mot
fichier = open("fichier.txt", "r")
contenu = fichier.read()
mots = contenu.split(" ")
for mot in mots:
    print(mot)
fichier.close()
```