#11.Container With Most Water
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxAr = 0
        l = 0
        r = len(height) - 1
        while l < r:
            minLine = min(height[l], height[r])
            maxAr = max(maxAr, minLine * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxAr
