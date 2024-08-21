class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            # check the current number with the previous one, if they are the same just increment the r pointer
            if nums[r] == nums[r - 1]:
                continue
            
            # if they are not the same then we need to swap the right num with where ever the left one standing and then increment the position of the left pointer
            nums[l] = nums[r]
            l += 1
        
        return l