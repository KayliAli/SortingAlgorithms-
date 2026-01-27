# selecition sorted(karşılaştırarak sıralama algoritması)

# 1.adım bir liste olsun 3,5,8,4 ve ilk elemanı x1=3 alınacak:(x2=5,x3=8,x4=4);
# 2.adım x1;x2,x3,x4 ile karşılaştırılacak.
# 3.adım x2;x3,x4 ile karşılaştırılacak
# 4.adım x3;x4 ile karşılaştırılacak
# 5. adım x4 son oldugundan x1,x4,x2,x3 olarak sıralanacak.

def selecition_sorted(liste):
    for j in range(0,len(liste)):
        for i in range(len(liste)):
            if liste[j]<liste[i]:
                liste[j],liste[i]=liste[i],liste[j]

            
    return liste

liste1=list(map(int, input("Lütfen bir liste giriniz(',')->").split(",")))
print(liste1)
sirali_list=selecition_sorted(liste1)
print(sirali_list)

