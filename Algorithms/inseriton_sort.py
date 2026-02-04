def insertion_sort(arr):
    for ilk_eleman in range(1, len(arr)):
        anahtar_deger = arr[ilk_eleman]  # Anahtar değer, şu anki eleman olmalı
        kiyaslanan_karakter = ilk_eleman - 1

        while kiyaslanan_karakter >= 0 and arr[kiyaslanan_karakter] > anahtar_deger:
            arr[kiyaslanan_karakter + 1] = arr[kiyaslanan_karakter]  # Bir sağa kaydırma
            kiyaslanan_karakter -= 1
        
        arr[kiyaslanan_karakter + 1] = anahtar_deger  # Anahtar değeri doğru pozisyona yerleştirme
    
    return arr


