from collections import Counter


def gyakori(honapok):
    gyakorisag = Counter(honapok)
    leggyakoribb = gyakorisag.most_common(3)
    return leggyakoribb


def kiiras(leggyakoribb, honapok):
    print('A három leggyakoribb születési hónap fordított sorrendben: ')
    print(leggyakoribb[2][0] + '.hó-', str(round(leggyakoribb[2][1] / len(honapok) * 100, 1)) + '%;  ',
          leggyakoribb[1][0] + '.hó-',
          str(round(leggyakoribb[1][1] / len(honapok) * 100, 1)) + '%;  ', leggyakoribb[0][0] + '.hó-',
          str(round(leggyakoribb[0][1] / len(honapok) * 100, 1)) + '%;  ')
    print('----------------------------------------------------')


def main():
    print('Melyik a három leggyakoribb születési hónap ezen űrhajósok körében?')
    print('----------------------------------------------------------------------')
    honapok = []
    with open('astronauts.csv') as forrasfajl:
        nagy_lista = forrasfajl.readlines()
    for sor in nagy_lista:
        darabolt = sor.strip().split(',')
        egybe_ido = darabolt[4]
        ido_darabolva = egybe_ido.strip().split('/')
        honap = ido_darabolva[0]
        honapok.append(honap)
    leggyakoribb = gyakori(honapok)
    kiiras(leggyakoribb, honapok)


main()