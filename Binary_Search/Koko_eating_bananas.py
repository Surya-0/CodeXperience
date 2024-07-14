class Solution:
    def minEatingSpeed(self, piles: 'List[int]', h: int) -> int:
        max_ban = max(piles)
        low = 1
        high = max_ban
        res = max_ban
        while low <= high:
            mid = low + (high - low) // 2
            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid

            if hours <= h:
                res = min(mid, res)
                high = mid - 1

            else:
                low = low + 1

        return res

    # A C++ solution
""""
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        long long max_ban = *max_element(piles.begin(), piles.end());
        long long low = 1;
        long long high = max_ban;
        long long res = max_ban;
        while (low <= high) {
            long long mid = low + (high - low) / 2;
            long long hours = 0;
            for (int p : piles) {
                hours += (static_cast<long long>(p) + mid - 1) / mid;
            }
            if (hours <= h) {
                res = min(mid, res);
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return static_cast<int>(res);
    }
};"""