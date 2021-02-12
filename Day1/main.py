if __name__ == '__main__':


    fichier = open('input.txt', 'r')
    content = fichier.read()
    tableau = [ int(i) for i in content.split('\n')]

    for x in tableau:
        for y in tableau:
            for z in tableau:
                if x+y+z == 2020:
                    print(x*y*z)
