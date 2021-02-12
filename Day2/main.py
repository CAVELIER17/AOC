if __name__ == '__main__':

    fichier = open('input.txt', 'r')
    content = fichier.read()
    tableau = [str(i) for i in content.split('\n')]
    nbmdp = 0
    nbmdpT = 0

    for x in tableau:
        ligne = x.split(': ')
        mdp = str(ligne[1])
        lettre = ligne[0].split(' ')
        num = [int(t) for t in lettre[0].split('-')]

        prenum = mdp[num[0]-1] == lettre[1]
        deunum = mdp[num[1]-1] == lettre[1]
        if prenum ^ deunum:
            nbmdpT = nbmdpT + 1

    print(nbmdpT)
