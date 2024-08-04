arr = [2,3,1,6,4,5]
n = len(arr)
for i in range(n):
    swapped = False
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
            swapped = True
    print(arr)
    if not swapped:
        break
print(arr)