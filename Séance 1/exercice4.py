score_lettres = [
    (['?'], 0),
    (['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u'], 1),
    (['d', 'g', 'm'], 2),
    (['b', 'c', 'p'], 3),
    (['f', 'h', 'v'], 4),
    (['j', 'q'], 8),
    (['k', 'w', 'x', 'y', 'z'], 10)
]

def score(mot):
    if len(mot) == 1:
        for (lettres, s) in score_lettres:
            if mot[0] in lettres:
                return s
    s = 0
    for c in mot:
        s += score(c)
    return s

def max_score(liste_mots):
    max_score = 0
    max_mot = ""
    for mot in liste_mots:
        s = score(mot)
        if s > max_score:
            max_score = s
            max_mot = mot
    return (max_mot,max_score)

print(max_score(['rte', 'ver', 'ce', 'etc', 'cet', 'ex', 'cr', 'et', 'ter', 'te', 'ct']))