class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = nums.copy()

        for j in range(len(nums)):
            nums[(j + k) % len(nums)] = tmp[j]   