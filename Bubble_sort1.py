#bubble sort


liste=[3,8,5,7,10,9,1,0,-2]
kontrol=False
while kontrol==False:
    kontrol=True
    for i in range(len(liste)-1):
        if liste[i]>liste[i+1]:
            kontrol=False
            liste[i],liste[i+1]=liste[i+1],liste[i]

print(liste)