
def left_child(i):
    return i*2 + 1


def right_child(i):
    return i*2 + 2


def parent(i):
    return (i-1)//2

def insert(heap,data):
    heap.append(data)
    return heapify_up(heap,len(heap)-1)

def heapify_up(heap, i):
    co=ini=0
    while i > 0 and heap[i] < heap[parent(i)]:
        co+=1
        ini+=1
        heap[i], heap[parent(i)] = heap[parent(i)], heap[i]
        i = parent(i)
    return co,ini

def heapify(heap, i):
    co=ini=0
    co1=ini1=0
    length = len(heap)
    min_ = i

    left = left_child(i)
    right = right_child(i)

    if left < length and heap[left] < heap[min_]:
        min_ = left

    if right < length and heap[right] < heap[min_]:
        min_ = right
    co+=2
    if min_ != i:
        ini+=1
        heap[i], heap[min_] = heap[min_], heap[i]  
        co1,ini1=heapify(heap, min_) 
    return co1+co,ini1+ini


def remove_root(heap):
    co=ini=0
    if len(heap) == 0:
        return None,0,0 
    head = heap[0]
    ini+=1
    heap[0] = heap[-1]
    heap.pop()  
    count= heapify(heap, 0)

    return head,co+count[0],ini+count[1]


def build_heap(arr):
    co=ini=0
    heap=[]
    for i in arr:
        count=insert(heap,i)
        co+=count[0]
        ini+=count[1]
    return heap,co,ini


def heap_sort(arr):
    heap,co,ini= build_heap(arr)
    for i in range (len(heap)):
        res = remove_root(heap)
        arr[i]= res[0]
        co+=res[1]
        ini+=res[2]
    return co,ini
    
        

arr=[5, 6, 4, 8, 9, 7, 1, 2, 3]
print(heap_sort(arr))
print(arr)


