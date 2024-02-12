class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = math.inf
        
        s = 0
        l = 0
        for r in range(len(nums)):
            n = nums[r]
            
            # calculating the sum
            s += n
            
            while s >= target:
                # find the min ans
                mm = (r - l + 1)
                ans = min(ans, mm)
                
                # removing from left
                s -= nums[l]
                
                l += 1
        
        return ans if ans != math.inf else 0