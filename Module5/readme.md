## Les fonctions

Les fonctions permettent de regrouper des instructions qui peuvent être réutilisées plusieurs fois dans un programme. Pour créer une fonction, il suffit d'utiliser le mot-clé `def`.

```python
# Exemple de fonction
def dire_bonjour():
    print("Bonjour !")

# Appel de la fonction
dire_bonjour()
```

Il est possible de passer des paramètres à une fonction.

```python
# Exemple de fonction avec paramètres
def dire_bonjour(nom):
    print("Bonjour " + nom + "!")

# Appel de la fonction
dire_bonjour("Jean")
```

Il est possible de retourner une valeur à partir d'une fonction.

```python
# Exemple de fonction avec retour de valeur
def dire_bonjour(nom):
    return "Bonjour " + nom + "!"

# Appel de la fonction
message = dire_bonjour("Jean")
print(message)
```

Il est possible de définir des valeurs par défaut pour les paramètres d'une fonction.

```python
# Exemple de fonction avec valeurs par défaut
def dire_bonjour(nom=""):
    return "Bonjour " + nom + "!"

# Appel de la fonction
message = dire_bonjour()
print(message)
```

### Atelier 1

```python
def isPalindrome(string):
    # TODO: Écrire le code ici

result1 = isPalindrome("kayak") # true
result2 = isPalindrome("laval") # true
result3 = isPalindrome("bonjour") # false
result4 = isPalindrome("radar") # true
result5 = isPalindrome("rotor") # true
```

### Atelier 2

```python
def sumOfTwoDigitsInTheTable(array, sum):
    # TODO: Écrire le code ici

result1 = sumOfTwoDigitsInTheTable([1, 8, 3, 6, 9, 2, 5, 12], 9)
result2 = sumOfTwoDigitsInTheTable([1, 1, 3, 6, 9, 2, 5, 12], 14)
result3 = sumOfTwoDigitsInTheTable([1, 80, 3, 6, 9, 2, 6, 12], 17)
result4 = sumOfTwoDigitsInTheTable([1, 90, 9, 6, 32, 2, 5, 12], 18)

print(result1)
print(result2)
print(result3)
print(result4)
```

### Atelier 3

```python
def isValidClosure(string):
    # TODO: Écrire le code ici
    

result1 = isValidClosure("{([{}])}") # true
result2 = isValidClosure("([)]") # false
result3 = isValidClosure("{[])") # false
result4 = isValidClosure("{[{[({()})]}]}") # true
result5 = isValidClosure("{[{[({()})]}]]") # false

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
```