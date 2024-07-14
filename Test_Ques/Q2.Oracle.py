"""
In Geek-land, there are m flight routes with n airport terminals. ¡th flight route will connect
airport terminal a; to b; incurring cost ci. Now the king of Geek-land wants to start a flight from
airport terminal 1 which will stop at terminal n. Help him calculate the maximum possible cost
on a finite route he may need to spend and If not possible return -1.
Example 1:
Input: n = 5, m=7, routes = {{1,2,9},{1,3,10},
{1,4,2},{1,5,6},{2,4,14},{2,5,2},{4,5,11}}
Output: 34
Explanation: Maximum possible total cost can
be 34 if flight will take the route as
1->2->4->5 = 9 +14 +11 = 34.
Example 2:
0
Input: n = 5, m=4,routes = {{1,5,1},{2,5,7},
(3,4,6}{3.5.13}},
Output: 1
"""

# The time complexity will be O(n+m)

from collections import defaultdict, deque


def max_cost_route(n, m, routes):
    adList = defaultdict(list)
    for u, v, route_dist in routes:
        adList[u].append((v, route_dist))

    print("Adjacency List is : ", adList)
    # Finding the in-degree
    in_degree = defaultdict(int)

    for u in adList:
        # print(u)
        # print(adList[u])
        for v in adList[u]:
            ele = v[0]
            # print(ele)
            in_degree[ele] += 1
    print("In degree is : ", in_degree)
    # Topological sort
    queue = deque()
    queue.append(1)
    dist = [-float('inf')] * (n + 1)
    dist[1] = 0
    while queue:
        u = queue.popleft()
        for v, route_dist in adList[u]:
            new_dist = route_dist + dist[u]
            if new_dist > dist[v]:
                dist[v] = new_dist
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    return dist[n] if dist[n] != -float('inf') else -1


n1 = 5
m1 = 7
routes1 = [(1, 2, 9), (1, 3, 10), (1, 4, 2), (1, 5, 6), (2, 4, 14), (2, 5, 2), (4, 5, 11)]

n2 = 5
m2 = 4
routes2 = [(1, 5, 1), (2, 5, 7), (3, 4, 6), (3, 5, 13)]
print("Max cost for the routes 1 is : ", max_cost_route(n1, m1, routes1))
print()
print("Max cost for the routes 2 is : ", max_cost_route(n2, m2, routes2))
