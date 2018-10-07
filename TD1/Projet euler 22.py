def ordered_listing(file):
    
    "renvoie une liste de mots classés par ordre alphabétique à partir d'un fichier texte"
    
    f = open(file, 'r')
    L =[]
    for ligne in f :
        for presquemot in ligne.split(","):         #séparateur virgule attend dans le txt
            L += [presquemot[1:-1]]                 #enlève les guillemets encadrant les mots
    return sorted(L)

def solve(file):
    "renvoie la somme de : position_mot_dans_la_liste * somme_du_classement_lettres_dans_alphabet_du_mot pour chaque mot du fichier texte"
    
    score = 0
    for mot in ordered_listing(file):
        sum_of_letters = 0
        for letter in mot:
            sum_of_letters += ord(letter)-64
        score += sum_of_letters * (ordered_listing(file).index(mot)+1)
    return score


print (solve('p022_names.txt'))
