from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: 'List[str]', n: int) -> int:
        task_count = Counter(tasks)
        max_heap = [-i for i in task_count.values()]
        heapq.heapify(max_heap)

        time = 0
        cool_down = deque()

        while max_heap or cool_down:
            time += 1

            if max_heap:
                count = heapq.heappop(max_heap)
                count += 1

                if count < 0:
                    cool_down.append((count, time + n))

            if cool_down and cool_down[0][1] == time:
                heapq.heappush(max_heap, cool_down.popleft()[0])

        return time