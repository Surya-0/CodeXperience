class Solution(object):
    def calcArea(self, height, l, r):
        if height[l] < height[r]:
            return height[l] * (r - l)
        else:
            return height[r] * (r - l)

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        if height[l] < height[r]:
            area = height[l] * (r - l)
        else:
            area = height[r] * (r - l)

        while l <= r:
            if height[l] < height[r]:
                l = l + 1
                area = max(area, self.calcArea(height, l, r))

            else:
                r = r - 1
                area = max(area, self.calcArea(height, l, r))
        return area


