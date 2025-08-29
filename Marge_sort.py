#Morgen Sıralama Algoritması
# Bir liste alınır : [2,6,5,1,7,4,3]
# 1.adim liste 2 parçaya ayrılır a1=2,6,5,1   a2=7,4,3
# 2.adim a1 ve a2 kendi arasında ikiye bölünür
# a3=2,6 a4=5,1    a5=7,4  a6=3
# daha sonra 1 eleman kalana kadar yapılır
# recersuve fonksiyon ile yapılacak .


def Morgen_sort(liste1):

    if len(liste1)<=1:
        return liste1
    
    u=len(liste1)
    orta=round(u/2)
    sag=liste1[orta:]
    sol=liste1[:orta]
        # for x in range(0,orta):
        #     sol.append(liste1[x])
        # for y in range(orta,len(liste1)):
        #     sag.append(liste1[y])  

    sag=Morgen_sort(sag)
    sol=Morgen_sort(sol)
    sirali_liste=[]
    while sag and sol:
         if sag[0]<sol[0]:
             sirali_liste.append(sag[0])
             sag.pop(0)
             
         else:
            sirali_liste.append(sol[0])
            sol.pop(0)

    if sol:
        sirali_liste+=sol
    if sag:
        sirali_liste+=sag

    return sirali_liste


a=[1,3,5,2,7,8,6]
print(Morgen_sort(a))