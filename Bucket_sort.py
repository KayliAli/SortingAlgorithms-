# Bucket sort algoritması:
# Bucket yada 'kova' sıralama algoritması denir
# bu algoritma öncelikle listenin uzunlugu kadar bos kova yani bucket oluşturur.
# daha sonra bu elemnalarını index lerini bulur yani hangi kovaya gidecek
# daha sonra bir kovada başka elemanlar olabilir bu yüxden her kova kendi içinde siralanaır ve sırasıyla birleştirilir.

def insertion_sort(bucket):
    for x in range(1,len(bucket)):
        while bucket[x-1]>bucket[x] and x>0:
            bucket[x-1],bucket[x]=bucket[x],bucket[x-1]
            x-=1
    return bucket

def Bucket_sort(arr):
    n = len(arr)
    largest = max(arr)
    size = (largest / n)

    buckets = [[] for _ in range(n)]    

    for eleman in arr:
        index = int(eleman / size)    #her elemanın yerleşecegi index bulunabilir
        if eleman == largest:
            index = n - 1
        buckets[index].append(eleman)

    sirali_arr = []
    for bucket in buckets:
        sirali_arr.extend(insertion_sort(bucket))   # her kova kendi içinde sıralanır ve birleştirilir

    return sirali_arr

# Test     
arr = [30, 17, 97, 42, 4, 65, 37, 48, 92, 40]
print(Bucket_sort(arr))

