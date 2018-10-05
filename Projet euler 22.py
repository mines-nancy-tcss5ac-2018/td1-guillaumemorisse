def ordered_listing(file):
    "transforme le fichier texte en une liste de mots classés par ordre croissant"
    f = open(file,'r')
    L =[]
    for ligne in f :
        for presquemot in line.split(",") :
            L += presquemot[1:-1]

    return L.sort()

def solve(file):
    "je n'ai pas encore pu executer ce code car pyzo ne supportait pas lextraction du fichier txt "
    " à partir de la liste triée de mots, renvoie la somme : des produits des classements des mots avec la somme du rang de chacun des caractères des mots"
    "projet euler 22"
    score = 0
    for mot in ordered_listing(file) :
        sum_of_letters = 0
        for  letter in mot :
            sum_of_letters += ord(letter)-96
        score += sum_of_letters * (L.index(mot)+1)
    return score


print (solve('p022_names'))