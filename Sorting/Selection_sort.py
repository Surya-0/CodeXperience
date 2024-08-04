arr = [2,3,1,6,4,5]
n = len(arr)
for i in range(n):
    min_ind = i
    for j in range(i+1,n):
        if arr[min_ind] > arr[j]:
            min_ind = j
    arr[i],arr[min_ind] = arr[min_ind],arr[i]
print(arr)