# Time complexity of memoization is O(n) and time complexity
# of recursion is O(2^n) and space complexity of both is O(n

import time
d = dict()
d[2] = 1

def fibo(n):
    if n<=2 :
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
def fib_memo(n):
    if n in d:
        return d[n]

    if n<=2:
        return 1

    else:
        d[n] = fib_memo(n-1) + fib_memo(n-2)
        return d[n]

st = time.time()
val = 35
print(fib_memo(val))
et = time.time()
print("The time taken for the memo fib function is : ", et-st)
st = time.time()
print(fibo(val))
et = time.time()
print("The time taken for the normal fib function is : ", et-st)
