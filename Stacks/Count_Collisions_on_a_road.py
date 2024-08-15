class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        res = 0

        # Ignore all left-moving cars before we encounter any right-moving car
        i = 0
        while i < n and directions[i] == 'L':
            i += 1

        # Similarly, ignore all right-moving cars after we encounter all other cars
        j = n - 1
        while j >= 0 and directions[j] == 'R':
            j -= 1

        # Now we only care about the middle part of the string that has potential collisions
        for k in range(i, j + 1):
            if directions[k] != 'S':
                res += 1

        return res
