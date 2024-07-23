import heapq
arr = [10,7,2,4,5,1,0]
heapq.heapify(arr)
print(arr)
heapq.heappop(arr)
print(arr)
while arr:
    print(heapq.heappop(arr))