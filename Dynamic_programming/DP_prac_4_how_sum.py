from collections import defaultdict

"""Time complexity of the recursive function is O(n^m*m) where m is the number of elements in the array and n is the 
target sum.The space complexity is O(m). The time complexity is O(n*m*m) and space complexity is O(m*m)"""


def howsum(targetSum, numbers):
    if targetSum == 0:
        # print("target sum is : ",targetSum)
        return []
    if targetSum < 0:
        # print("target sum is : ",targetSum)
        return None

    for num in numbers:
        rem = targetSum - num
        # print(rem)
        res = howsum(rem, numbers)
        if res != None:
            res.append(num)
            return res
    # print("hi")
    return None


d = defaultdict(list)
d[0] = []


def howsum_memo(targetSum, numbers):
    if targetSum in d:
        return d[targetSum]

    if targetSum < 0:
        return None

    for num in numbers:
        rem = targetSum - num
        res = howsum_memo(rem, numbers)
        if res != None:
            res.append(num)
            d[targetSum] = res
            return d[targetSum]

    return None


print(howsum(7, [2, 3]))
print(howsum(7, [5, 3, 4, 7]))
print(howsum(7, [2, 4]))

print("___________________________________")

print(howsum_memo(7, [2, 3]))
