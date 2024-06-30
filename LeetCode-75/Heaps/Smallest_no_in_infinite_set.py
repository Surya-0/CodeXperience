import heapq
class SmallestInfiniteSet:

    def __init__(self):
        self.infset = {i for i in range(1,1001)}
        self.min_heap = [i for i in range(1,1001)]
        heapq.heapify(self.min_heap)

    def popSmallest(self) -> int:
        ele = heapq.heappop(self.min_heap)
        self.infset.remove(ele)
        return ele

    def addBack(self, num: int) -> None:
        if num not in self.infset:
            self.infset.add(num)
            heapq.heappush(self.min_heap,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)