# Bogo sıralama Algoritması

import random as rd


def bogo_sort(ls):
    sayac=0
    kontrol=False
    while kontrol!=True:
        rd.shuffle(ls)
        sayac+=1

        if ls==sorted(ls):
            kontrol=True
            print(ls,"try:",sayac)


