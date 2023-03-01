class Solution:
    def merge_sort(self, nums: List[int], l: int, r: int) -> List[int] :
        
        def merge_me_daddy(nums: List[int], left: int, mid: int, right: int):
            # we have to merge the left and right sides, daddy!
            l = nums[left:mid+1]
            r = nums[mid+1:right+1]
            
            # j : left, k : right
            i, j, k = left, 0, 0
            
            while j < len(l) and k < len(r):
                if l[j] <= r[k]:
                    nums[i] = l[j]
                    j += 1
                else:
                    nums[i] = r[k]
                    k += 1
                i += 1
            
            # the rest of the items left in both left and right if exist
            while j < len(l):
                nums[i] = l[j]
                j += 1
                i += 1
            
            while k < len(r):
                nums[i] = r[k]
                k += 1
                i += 1             
        
        if l == r:
            return nums
        
        # divide
        m = (l + r) // 2
        self.merge_sort(nums, l, m)
        self.merge_sort(nums, m + 1, r)
        
        # mergeeeeeee
        merge_me_daddy(nums, l, m, r)
        
        return nums
        
        
    # quick sort using the pivot
    # for some reasons, it's giving me time limit lol
    def quick_sort(self, nums: List[int]) -> List[int]:
        # base case
        if len(nums) <= 1:
            return nums
        else:
            pivot = nums.pop()

        # the numbers bigger than the pivot
        large_nums = []

        # the numbers smaller than the pivot
        smol_nums = []

        for num in nums:
            if num > pivot:
                large_nums.append(num)
            else:
                smol_nums.append(num)

        return quick_sort(smol_nums) + [pivot] + quick_sort(large_nums)
    
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums, 0, len(nums) - 1)