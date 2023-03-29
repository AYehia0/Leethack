class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = 0
        
        # brute force solution, try all the until one is right (RETURN)
        for i in range(pow(2, len(nums))):
            # converting to base 2 BIN
            tmp = bin(i)[2:].zfill(len(nums))
            
            if tmp not in nums:
                return tmp
            
        return "wtf"