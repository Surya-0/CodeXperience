# In how many ways can we travel from the top left corner to the bottom right corner in a m x n grid?We can only move
# to the right or down When we move right the number of columns reduce and when we move down the number of rows
# reduce The time complexity of the normal grid traveller function is O(2^(m+n)).The time complexity of the memoized
# function is O(m+n). The space complexity of the normal grid function is O(m+n) and the space complexity of the
# memoized function is O(mn)


import time


def grid_traveller(m, n):
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    return grid_traveller(m - 1, n) + grid_traveller(m, n - 1)


d = dict()
d[(1, 1)] = 1
d[(0, 1)] = 0
d[(0, 0)] = 0
d[(1, 0)] = 0


def grid_traveller_memo(m, n):
    if (m, n) in d:
        return d[(m, n)]

    if m == 1 and n == 1:
        return 1

    if m == 0 or n == 0:
        return 0

    d[(m, n)] = d[(n, m)] = grid_traveller_memo(m - 1, n) + grid_traveller_memo(m, n - 1)
    return d[(m, n)]


print("Done using normal grid traveller function")
st = time.time()
print(grid_traveller(3, 2))
print(grid_traveller(5, 4))
print(grid_traveller(12, 13))
et = time.time()
print("The time taken using normal function is : ", et - st)

print("\n")

print("Done using memoization")
st = time.time()
print(grid_traveller_memo(3, 2))
print(grid_traveller_memo(5, 4))
print(grid_traveller_memo(12, 13))
et = time.time()
print("The time taken using memoization is : ", et - st)
# print(grid_traveller(18,18))
