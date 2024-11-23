# def insertion_sort(arr):
#     comparisons_count = 0
#     initializations_count = 0

#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j >= 0:
#             comparisons_count += 1
#             if arr[j] > key:
#                 initializations_count += 1
#                 arr[j+1] = arr[j]
#                 comparisons_count -= 1

#             elif arr[j] < key:
#                 initializations_count += 1
#                 arr[j+1] = key
#                 break
#             comparisons_count += 1
#             initializations_count += 1
#             j -= 1

#         arr[j+1] = key

#     return comparisons_count,initializations_count


def insertion_sort(arr):
    comparisons_count = 0
    initializations_count = 0
    
    for i in range(1, len(arr)):
        key = arr[i]
        initializations_count += 1 
        j = i - 1
        
        while j >= 0 and arr[j] > key:  
            comparisons_count += 1
            arr[j + 1] = arr[j]  
            initializations_count += 1
            j -= 1
        
        arr[j + 1] = key  
        initializations_count += 1
        
        if j >= 0:
            comparisons_count += 1
    
    return comparisons_count, initializations_count
