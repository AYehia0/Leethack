import math 

class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        l = 0  # left pointer
        r = 0  # right pointer
        
        while r < len(nums) - 1:
            max_jump = 0
            for i in range(l, r + 1):
                max_jump = max(max_jump, i + nums[i])
            l = r + 1
            r = max_jump
            jumps += 1
            
        return jumps