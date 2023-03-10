class Solution:
    def trap(self, height: List[int]) -> int:
        """
        The optimal solution O(n) time, can be solved using 2 pointers.
        to calculate the water at i : min(max_left, max_right) - height[i]
        where max_right and left are max height right/left i
        
        There are 2 approaches for memory : O(n) and O(1)
        
        for the linear space, we can create 2 lists for calculating both left_max and right_max, then use the above equation.
        """
        
        
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        ans = 0
        
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                ans += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                ans += max_r - height[r]
                
        return ans