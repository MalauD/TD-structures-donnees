tirage = ['a', 'o', 'f', 'v', 'i', 'o', 'e', 'r']
mots_possibles = ['sacre', 'sabre', 'baser', 'cabre', 'garce', 'crase', 'brase', 'barge', 'caser', 'jaser', 'crabe', 'scare', 'aber', 'gare', 'sage', 'gars', 'rase', 'arec', 'acre', 'jars', 'case', 'base', 'cage', 'rage', 'jase', 'bras', 'race', 'ars', 'sac', 'arc', 'are', 'jar', 'jas', 'bar', 'bas', 'ace', 'cas', 'car', 'age', 'bac', 'cab', 'as', 'ra', 'sa', 'a']

def mot_possible(lexique, tirage):
    # On garde en mémoire le mot le plus long
    mot_le_plus_grand = ""
    for mot in lexique:
        mot_dans_lexique = True
        tirage_en_cours = tirage.copy()
        # On vérifie que chaque lettre du mot courant est dans le tirage
        for c in mot:
            if c not in tirage_en_cours:
                mot_dans_lexique = False;
                break
            tirage_en_cours.remove(c)
        # Si le mot courant est plus long on remplace
        if mot_dans_lexique and len(mot) > len(mot_le_plus_grand):
            mot_le_plus_grand = mot
    return mot_le_plus_grand

print("Test n°1")
print(mot_possible(mots_possibles, tirage))

def read_file(chemin):
    liste = []
    f = open(chemin)
    for ligne in f:
        # On enlève le \n de chaque fin de ligne
        mot = ligne.rstrip()
        if len(mot) <= 8:
            liste.append(mot)
    return liste


print("Test n°2")
mots_possibles = read_file("mots.sansaccent.txt")
print(mot_possible(mots_possibles, tirage))



            