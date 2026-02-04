from Algorithms.Selection_sort import selecition_sorted
from Algorithms.Bubble_sort1 import bubble_sort
from Algorithms.Bogo_sort import bogo_sort
from Algorithms.inseriton_sort import insertion_sort
from Algorithms.Marge_sort import morgen_sort
from Algorithms.Bucket_sort import Bucket_sort
from Algorithms.Quick_sort import quick_sort
from Algorithms.Radix_sort import radix_sort
from Algorithms.MaxHeap_sort import max_heap_sort
from Algorithms.Counting_sort import counting_sort
from Algorithms.Shake_sort import shake_sort
from Algorithms.Stooge_sort import stooge_sort


arry=[2,25,0,156,89,7,65,10,11]

if __name__=="__main__":

    print("Selction Sort",selecition_sorted(arry))
    print("Bubble Sort",bubble_sort(arry))
    print("Insertion Sort",insertion_sort(arry))
    print("Morang Sort",morgen_sort(arry))
    print("Quick Sort",quick_sort(arry))
    print("Radix Sort",radix_sort(arry))
    print("Max Heap Sort",max_heap_sort(arry))
    print("Counting Sort",counting_sort(arry))
    print("Shake_Sort",shake_sort(arry))
    print("Stooge_Sort",stooge_sort(arry))
    print("Bogo_Sort",bogo_sort(arry))
    print("Bucket Sort",Bucket_sort(arry))