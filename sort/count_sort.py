def count_sort(arr):

    initializations_count = 0

    min_, max_ = min(arr), max(arr)
    c = [0 for _ in range(max_-min_+1)]

    for i in arr:
        initializations_count += 1
        c[i-min_] += 1

    for i in range(1, len(c)):
        initializations_count += 1
        c[i] += c[i-1]

    b = [None]*(len(arr))

    for j in range(len(arr) - 1, -1, -1):
        initializations_count += 2
        b[c[arr[j]-min_]-1] = arr[j]
        c[arr[j]-min_] -= 1
    
    return 0,initializations_count


