# counting Sıralam algoritması:
# bu sıralama algoritmasına bir başka deyişle 'sayarak sıralama ' denir
# bu algoritmanın en önemli özelligi : bir karşılaştırma koşulu içermemesidir:
# öncelikle listenin her bir elemanın ne kadar tekrar ettigi bulunur.
# daha sonra bu tekrar listesinden her eleman kendinden önceki-
#elemanla toplanıp 'cumlative_sum' adında bir liste oluşturulur
#daha sonra sıralanacak olan listenin en son elemannıdan başlanarak-
# cumalative_sum daki degerinden -1 çıkartarak index i bulunur 
# ve bu her eleman için gerçekleşir


def counting_sort(ls):
    counter=[]
    max_sayi=max(ls)        # her rakamdan kaç tane oldugunu tutan liste
    for i in range(max_sayi+1):
        tekrar=ls.count(i)
        counter.append(tekrar)
    
    cumalative_sum=[0 for _ in range(len(counter))]  
    
    toplam=0
    for i in range(len(counter)):
        toplam+=counter[i]
        cumalative_sum[i]=toplam
    
    sirali_liste = [0 for _ in range(len(ls))]

    for eleman in ls[::-1]:
        index=cumalative_sum[eleman]-1
        sirali_liste[index]=eleman
        cumalative_sum[eleman]-=1
    

    return sirali_liste


ls=[2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
print(ls)
print(counting_sort(ls))

















