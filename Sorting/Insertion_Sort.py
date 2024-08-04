arr = [2,3,1,6,4,5]
for i in range(len(arr)):
    temp = arr[i]
    j = i - 1
    while j >=0 and temp < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = temp

print(arr)

