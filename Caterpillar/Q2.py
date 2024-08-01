arr = [3,2,0,1]
brr = [0] * len(arr)
for i,val in enumerate(arr):
    brr[val] = i
print(brr)