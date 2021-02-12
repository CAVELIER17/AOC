if __name__ == '__main__':

    fichier = open('input.txt', 'r')
    content = fichier.read()
    tableau = [str(i) for i in content.split('\n')]

    nbX = 0
    nby = 0
    nbArbre=0
    Dtab = len(tableau[1])


    for x in tableau:
        if nbX>=Dtab:
            nbx = nbX-Dtab
        nbX = nbX + 3
        print(x[nbX])
        if x[nbX] != '.':
            nbArbre = nbArbre +1
