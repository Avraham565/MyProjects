from random import randint

def merge(arr,start,end):
    mid=start+((end-start)//2)
    comparisons_count=initializations_count=0
    i=j=0
    k=start
    right= arr[start:mid+1]
    left= arr[mid+1:end+1]
    while i < len(left) and j < len(right):
        comparisons_count+=1
        if left[i] < right[j] :
            arr[k]= left[i]
            i+=1
        else:
            arr[k] = right[j]
            j+=1
        initializations_count+=1
        k+=1
    while i < len(left):
        arr[k]= left[i]
        i+=1
        k+=1
        initializations_count+=1
    while j < len(right):
        arr[k]= right[j]
        j+=1
        k+=1
        initializations_count+=1
    return comparisons_count,initializations_count

            
        

def _merge_sort(arr, s, e):
    if s >= e:
        return 0,0
    mid= s+((e-s)//2)
    c1, i1=_merge_sort(arr,s,mid)
    c2, i2=_merge_sort(arr,mid+1,e)
    c,i= merge(arr,s,e)

    return c+c1+c2, i+i1+i2

  
    
        


        

    
    
def merge_sort(arr):
    comparisons_count,initializations_count=_merge_sort(arr, 0, len(arr)-1)
    return comparisons_count,initializations_count

arr=[(randint(1,1000)) for _ in range(100)]
print(merge_sort(arr))
print(arr)