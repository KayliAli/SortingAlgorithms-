# radix sıralama algoritması
# 3 basamaklı sayılardan oluşan bie liste al
# [112,129,305,426]
# [1] [2] [3] [4] [5] [6] [7] [8] [9] [0] 

def birlestirme(C):
    liste=[]
    for i in range(10):
        uz=len(C[i])
        if uz!=0:
          for j in range(uz):
            liste.append(C[i][j])
    
    return liste


def radix_sort(liste):

    maks=max(liste)
    basamak_sayisi=len(str(maks))


    for i in range(basamak_sayisi):
        C=[[] for x in range(10)]
        for sayi in liste:
            num=sayi//10**(i)%10
            C[num].append(sayi)
        E=birlestirme(C)

    print(E)

liste=[624,211,125,132,395,458]
radix_sort(liste)