#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
from os.path import getsize


# TODO: Définissez vos fonction ici
def mot_plus_long(f_name):
    with open(f_name, mode='r') as f:
        mots = f.read().split()
        mots.sort(key=lambda x: len(x), reverse=True)

    return print(mots[0])


def nombres_du_fichier(f_name):
    with open(f_name, mode='r') as f:
        donnees = f.read()

    mots = donnees.split()
    liste_nombres = []
    for mot in mots:  # vérifier si c'est des mots ou non
        if mot.isdigit():
            liste_nombres.append(int(mot))

    print(sorted(liste_nombres))

def comparer_fichiers(f1_name, f2_name):
    with open(f1_name, "r") as f1, open (f2_name, "r") as f2:
        f1.seek(0, 2)
        f2.seek(0, 2)
        print(f1.tell(), f2.tell())
        f1.seek(0)
        f2.seek(0)

    f1 = open(f1_name, "r")
    f2 = open(f2_name, "r")

    car1 = f1.read(1)
    car2 = f2.read(1)

    while car1 != ' ' and car2 != ' ':
        if car1 != car2:
            print(f"La différence est {car1} avec {car2}")
        car1 = f1.read(1)
        car2 = f2.read(1)

    f1.close()
    f2.close()

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    #comparer_fichiers(f1_name='exemple.txt', f2_name='exemple2.txt')

    #nombres_du_fichier(f_name='exemple.txt')

    mot_plus_long(f_name='exemple.txt')
