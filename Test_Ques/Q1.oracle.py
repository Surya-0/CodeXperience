"""
Geek's School is going to conduct a fest soon, for this fest's advertisement school needs some
number of posters represented by NUM. Geek's class is appointed to make all the posters for the
fest, class has N students each student can make one poster in some amount of time, which is
represented by an integer array time of length N.
Every student will start making the second poster as soon as he/she gets finished with the first
one and so on. You need to find the minimum amount of time so that all the students together
have made at least NUM number of posters.
Example 1:
Input:
N = 4
NUM = 10
time[] = {2, 3, 1, 4}
Output:
6
"""


def min_time_to_make_posters(N, NUM, time):
    def posters_by_time(t):
        temp = 0
        for val in time:
            temp += (t // val)
        return temp

    low = 1
    high = max(time) * NUM
    while low < high:
        mid = (low + high) // 2
        res = posters_by_time(mid)

        if res >= NUM:
            high = mid - 1
        else:
            low = mid + 1

    print("Low : ",low, "High : ",high)
    return low


N1 = 4
NUM1 = 10
time1 = {2, 3, 1, 4}

N2 = 1
NUM2 = 5
time2 = {1}
print("The min time to make posters for NUM1 is : ",min_time_to_make_posters(N1, NUM1, time1))
print("The min time to make posters for NUM2 is :",min_time_to_make_posters(N2,NUM2,time2))
