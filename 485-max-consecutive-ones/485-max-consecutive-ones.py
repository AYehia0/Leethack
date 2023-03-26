class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(set(nums)) == 1 and nums[0] == 0:
            return 0
        
        ans = 0
        count = 0
        
        for n in nums:
            if n == 1:
                count += 1
            else:
                ans = max(ans, count)
                count = 0

        ans = max(ans, count)
        
        return ans