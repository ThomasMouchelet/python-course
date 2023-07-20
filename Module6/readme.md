## Orienté objet

### Introduction

L'orienté objet est un paradigme de programmation qui permet de structurer son code en objets. Un objet est une entité qui possède des propriétés et des méthodes. Les propriétés sont des variables qui définissent l'état de l'objet et les méthodes sont des fonctions qui définissent le comportement de l'objet.

### Création d'une classe

Pour créer une classe, il suffit d'utiliser le mot-clé `class` suivi du nom de la classe. Le nom de la classe doit commencer par une majuscule.

```python
# Exemple de création d'une classe
class Personne:
    pass
```

### Création d'un objet

Pour créer un objet, il suffit d'appeler la classe comme si c'était une fonction.

```python
# Exemple de création d'un objet
class Personne:
    pass

personne = Personne()
```

### Ajout de propriétés

Pour ajouter une propriété à une classe, il suffit de définir une variable dans la classe.

```python
# Exemple d'ajout de propriétés
class Personne:
    nom = "Jean"
    age = 33

personne = Personne()
print(personne.nom)
print(personne.age)
```

### Ajout de méthodes

Pour ajouter une méthode à une classe, il suffit de définir une fonction dans la classe.

```python
# Exemple d'ajout de méthodes
class Personne:
    nom = "Jean"
    age = 33

    def parler(self):
        print("Bonjour, je m'appelle " + self.nom + " et j'ai " + str(self.age) + " ans.")

personne = Personne()
personne.parler()
```

### Constructeur

Le constructeur est une méthode qui est appelée lors de la création d'un objet. Pour créer un constructeur, il suffit de définir une méthode `__init__` dans la classe.

```python
# Exemple de constructeur
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self):
        print("Bonjour, je m'appelle " + self.nom + " et j'ai " + str(self.age) + " ans.")

personne = Personne("Jean", 33)
personne.parler()
```

### Héritage

L'héritage permet de créer une classe qui hérite des propriétés et des méthodes d'une autre classe. Pour créer une classe qui hérite d'une autre classe, il suffit de passer la classe parente en paramètre de la classe enfant.

```python
# Exemple d'héritage
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self):
        print("Bonjour, je m'appelle " + self.nom + " et j'ai " + str(self.age) + " ans.")

class Etudiant(Personne):
    pass

etudiant = Etudiant("Jean", 33)
etudiant.parler()
```

### Surcharge

La surcharge permet de modifier le comportement d'une méthode héritée. Pour surcharger une méthode, il suffit de définir une méthode avec le même nom dans la classe enfant.

```python
# Exemple de surcharge
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self):
        print("Bonjour, je m'appelle " + self.nom + " et j'ai " + str(self.age) + " ans.")

class Etudiant(Personne):
    def parler(self):
        print("Bonjour, je m'appelle " + self.nom + " et je suis étudiant.")

etudiant = Etudiant("Jean", 33)
etudiant.parler()
```

### Polymorphisme

Le polymorphisme permet de modifier le comportement d'une méthode héritée en fonction du type de l'objet. Pour utiliser le polymorphisme, il suffit de définir une méthode avec le même nom dans la classe enfant et de vérifier le type de l'objet.

```python
# Exemple de polymorphisme
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def parler(self):
        print("Bonjour, je m'appelle " + self.nom + " et j'ai " + str(self.age) + " ans.")

class Etudiant(Personne):
    def parler(self):
        print("Bonjour, je m'appelle " + self.nom + " et je suis étudiant.")

class Professeur(Personne):
    def parler(self):
        print("Bonjour, je m'appelle " + self.nom + " et je suis professeur.")

personne = Personne("Jean", 33)
etudiant = Etudiant("Jean", 33)
professeur = Professeur("Jean", 33)

personne.parler()
etudiant.parler()
professeur.parler()
```

### Atelier 1

Écrire un script Python qui permet à l'utilisateur de créer un compte bancaire. Le script doit demander à l'utilisateur de renseigner le nom du propriétaire du compte et le solde du compte. Le script doit ensuite afficher le nom du propriétaire du compte et le solde du compte. Le script doit ensuite demander à l'utilisateur de renseigner le montant du dépôt. Le script doit ensuite afficher le nouveau solde du compte.