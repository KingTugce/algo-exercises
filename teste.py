def disem_vowel(string):
    vowels = {"a","e","i","o","u"}
    liste = list(string)
    for v in vowels:
        while v in liste:
            liste.remove(v)
    return " ".join(liste)
disem_vowel('Hello World')