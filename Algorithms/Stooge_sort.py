# stooge sort Algoritması
# 1.adım listenin ilk elemanı ile son elemanı karşılaştırılır,ilk eleman dah büyükse swap yapılır.
# 2.adım listenin baştan 2/3 sıralanır
# 3. adım listenin sondan  2/3 sıralanır
# 4. adım tekrar baştan 2/3 sıralanır.

def stooge_sort(arr):
    def stooge(arr,i,j):  # i başlangıç index and j bitiş index
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
        
        if j - i + 1 <= 2:    # eger dizi 2 veya daha az elemanlı ise   dizi parçalamaya gerek yok zaten sıralanmıştır 
            return            # return yaparak fonksiyondan çıkılır  # (j-i+1)-> listenin uzunlugu yani len(arr) ile aynıdır
        
        k=(j-i+1)//3     # k degeri listeyi parçalamak için kullanılır.

        stooge(arr,i,j-k)
        stooge(arr,i+k,j)
        stooge(arr,i,j-k)
    stooge(arr,0,len(arr)-1)


arr=[64, 34, 25, 22, 11, 90]

print("original arry:",arr)

stooge_sort(arr)
print("sorted arry :",arr)

