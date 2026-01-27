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

ls=[1,2,5,0,4,3,9,7,8]
bogo_sort(ls)

