from collections import Counter


def bejaras_szetvalasztas(nagy_lista, foglalkozasok):
    for sor in nagy_lista:
        darabolt = sor.strip().split(',')
        foglalkozasok.append(darabolt[9])
        foglalkozasok.append(darabolt[10])
    for index, elem in enumerate(foglalkozasok):
        if elem == '' or elem == ' ':
            del foglalkozasok[index]


def eldontes_kiiras(foglalkozasok):
    # Három leggyakoribb foglalkozás
    gyakorisag = Counter(foglalkozasok)
    leggyakoribb = gyakorisag.most_common(3)
    print('Három leggyakoribb foglalkozás: ')
    print(leggyakoribb[0][0], str(round(leggyakoribb[0][1]/len(foglalkozasok)*100, 1))+'%,', leggyakoribb[1][0], str(round(leggyakoribb[1][1]/len(foglalkozasok)*100, 1))+'%,', leggyakoribb[2][0], str(round(leggyakoribb[2][1]/len(foglalkozasok)*100, 1)))
    print('----------------------------------------------------')
    # Három legritkább foglalkozás
    legritkabb = gyakorisag.most_common()[-3:]
    print('Három legritkább foglalkozás: ')
    print(legritkabb[0][0], str(round(legritkabb[0][1]/len(foglalkozasok)*100, 1))+'%,', legritkabb[1][0], str(round(legritkabb[1][1]/len(foglalkozasok)*100, 1))+'%,',legritkabb[2][0], str(round(legritkabb[2][1]/len(foglalkozasok)*100, 1)))


def main():
    print('A program kiírja a három leggyakoribb és a három legritkább foglalkozás ezen űrhajósok körében')
    print('----------------------------------------------------------------------')
    with open('astronauts.csv') as forrasfajl:
        nagy_lista = forrasfajl.readlines()
    foglalkozasok = []
    bejaras_szetvalasztas(nagy_lista, foglalkozasok)
    eldontes_kiiras(foglalkozasok)


main()
