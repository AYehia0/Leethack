class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        
        # [-1,0,1,2,-1,-4]
        # sorting first : [-1, -1, 0, 1, 2, 4]
        # fix a number and get 2Sum of the 2 others where x + y + z = 0 ==> y + z = 0
        # but since list is sorted we can use the 2 pointers
        
        for ind, num in enumerate(nums):
            # avoid dups
            if ind > 0 and num == nums[ind - 1]:
                continue
                
            l, r = ind + 1, len(nums) - 1
            while l < r:
                tmp = num + nums[l] + nums[r]
                
                if tmp == 0:
                    sol.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                
                if tmp >= 0:
                    r -= 1
                else:
                    l += 1
            
        
        return sol