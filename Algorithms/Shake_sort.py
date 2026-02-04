# cocktail_srot(shaker sort) Algoritması

# bu algoritma buble sortunun bir nevi bir çeşididir
#bu algoritmada çift yönlü bir tarama yapılır
# yani hem soldn saga dogru hemde sagdan sola dogru

def  shake_sort(liste):
    kontrol=True
    while kontrol:
        kontrol=False
        for i in range(len(liste)-1):
            if liste[i]>liste[i+1]:                      # ileri dogru tarama
                kontrol=False
                liste[i],liste[i+1]=liste[i+1],liste[i]
        

        for i in range(len(liste)-2,  - 1, -1):
            if liste[i] > liste[i + 1]:                       # geriye dogru tarama
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
                kontrol = False
        
        return liste


