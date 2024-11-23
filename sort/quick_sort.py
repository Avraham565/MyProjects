from random import randint

def randomise_partition(arr,p,r):
    co=0
    ini=0
    pivot= randint(p,r)
    arr[pivot], arr[r] = arr[r],arr[pivot]
    i=j=p
    k=r-1
    while j <= k:
        co += 1
        if arr[j] < arr[r]:
            ini+=1
            arr[j],arr[i]=arr[i],arr[j]
            i+=1
            j+=1
        elif arr[j] > arr[r]:
            ini+=1
            arr[k],arr[j] = arr[j],arr[k]
            k-=1
        else:
            j+=1
    ini+=1 
    arr[j], arr[r] = arr[r], arr[j]
    return i,k,co,ini


def _quick_sort(arr,p,r):
    if r-p <= 1:
        return 0,0
    i,k,co,ini=randomise_partition(arr,p,r)
    co1,ini1= _quick_sort(arr,p,i)
    co2,ini2= _quick_sort(arr,k+1,r)
    return co+co1+co2, ini1+ini2+ini

def quick_sort(arr):
    p=0
    r= len(arr)-1
    return(_quick_sort(arr,p,r))

