class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # using binary search
        
        # List : [1, 1, 2, 2, 3, 4, 4]
        # Index:  0  1  2  3  4, 5, 6
        # As you can see equal pairs starts with even index and ends with odd index
        # after the unique element 3 the index of the pairs starts with odd then even indcies
        # but how do we know it's unique ? : element at index (4) doesn't equal the el after or before it.
        # one more thing, if you are at index 3 (odd) and the current element equals the before, it's guaranteed that the unique element will never comes in that region [0-3], same for left side.
        
        # check the boundries
        if len(nums) == 1:
            return nums[0]
        if len(nums) >= 2 and nums[0] != nums[1]:
            return nums[0]
        
        if len(nums) >=2 and nums[-1] != nums[-2]:
            return nums[-1]
               
        # binary search
        low, high = 0, len(nums)-1
        while low <= high:
            # mid point
            mid = (low + high) // 2
            # is the mid element the unique one ?
            if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
               return nums[mid]
            
            if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (mid % 2 != 0 and nums[mid] == nums[mid - 1]):
               low = mid + 1
            else:
               high = mid - 1
        