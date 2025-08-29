# agaç yapısı

def maxheap(arr,n,i):
    largest=i
    left=2*i+1
    right=2*i+2

    if left<n and arr[largest]<arr[left]:
        largest=left
    if right<n and arr[largest]<arr[right]:
        largest=right
    if largest!= i:
        arr[largest],arr[i]=arr[i],arr[largest]
        maxheap(arr ,n ,largest)

arr=[2,15,9,30,18,6,25]
n=len(arr)

for i in range(n//2-1,-1,-1):
    maxheap(arr,n,i)

for i in range(n-1,0,-1):
    arr[0],arr[i]=arr[i],arr[0]
    maxheap(arr,i,0) #***dikkat


print(arr)

