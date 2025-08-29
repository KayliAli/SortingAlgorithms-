def quick_sort(ls):
    if len(ls)==1:
        return ls
    pivot=ls.pop(len(ls)//2) 
    sol=[]
    sag=[]

    for eleman in ls:
        if eleman<pivot:
            sol.append(eleman)
        else:
            sag.append(eleman)
    
    return quick_sort(sol)+[pivot]+quick_sort(sag)


a=[1,3,5,2,7,8,6]
print(quick_sort(a))