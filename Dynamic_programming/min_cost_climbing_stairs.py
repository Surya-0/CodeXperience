class Solution:
    def minCostClimbingStairs(self, cost: 'List[int]') -> int:
        # cost.append(0)

        # for i in range(len(cost)-3,-1,-1):
        #     cost[i] = min(cost[i]+cost[i+1],cost[i] + cost[i+2])

        # return min(cost[0],cost[1])

        cost.append(0)
        d = {0: cost[0], 1: cost[1]}
        n = len(cost)

        # print(n)
        def memo(i):
            if i in d:
                return d[i]

            d[i] = min(memo(i - 1), memo(i - 2)) + cost[i]
            return d[i]

        # print(d)
        return memo(n - 1)
        # return min(d[0],d[1])



