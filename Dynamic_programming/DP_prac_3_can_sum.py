""" The canSum function will take a target and a list of numbers and return if it
is possible to arrive at the target.Now we need to see if memoization is possible i.e., cache the results in
 a data structure. The time complexity of the canSum function is O(n^m) where n is the length of the number array and m is the
 target.The space complexity of the canSum function is O(m).The time complexity of the memoized canSum function is O(m*n) and the
space complexity of the memoized canSum function is O(m)"""


import time
d = dict()
d[0] = True

def canSum_memo(targetsum, nums):
    if targetsum in d:
        return d[targetsum]

    if (targetsum == 0):
        return True
    if targetsum < 0:
        return False

    for num in nums:
        res = targetsum - num
        if (canSum_memo(res, nums) == True):
            d[targetsum] = True
            return True

    d[targetsum] = False
    return False


def canSum(targetsum, nums):
    if (targetsum == 0):
        return True
    if targetsum < 0:
        return False

    for num in nums:
        res = targetsum - num
        if (canSum(res, nums) == True):
            return True

    return False

print("Done using normal canSum  function")
st = time.time()
print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(200, [7, 14]))
et = time.time()
print("The time taken using normal function is : ", et - st)
print()

print("Done using memoized canSum  function")
st = time.time()
print(canSum_memo(7, [2, 3]))
print(canSum_memo(7, [5, 3, 4, 7]))
print(canSum_memo(200, [7, 14]))
et = time.time()
print("The time taken using memoization is : ", et - st)