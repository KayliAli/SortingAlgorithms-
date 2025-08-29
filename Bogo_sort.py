# Bogo sıralama Algoritması

import random as rd

ls=[1,2,5,0,4,3,9,7,8]
sayac=0
kontrol=False
while kontrol!=True:
    rd.shuffle(ls)
    sayac+=1
        
    if ls==sorted(ls):
        kontrol=True
        print(ls,sayac)

