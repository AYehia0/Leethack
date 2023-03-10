class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_h = 0
        
        while l < r:
            # calculate the area
            area = abs(l - r) * min(height[r], height[l])
            max_h = max(max_h, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_h