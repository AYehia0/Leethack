class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m = defaultdict(int)
        
        for n in nums:
            m[n] += 1
            
        for k,v in m.items():
            if v > len(nums)/2:
                return k