import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # to check if the k is possible we round up : piles/possible-k if <= h it's valid solution, but we want to have the min k, we can use binary search to search in all the possible set of Ks [1...max(piles)] and shift to left half if found a solution less than k, if we finished piles in k > h we have to increase k by searching the right half part.
        
        # the max possible k : bananas/hour
        max_piles = max(piles)
        l, r = 1, max_piles
        ans = max_piles
        
        while l <= r:
            mid = (l + r) // 2
            rate = 0
            for p in piles:
                rate += math.ceil(p / mid)
                
            # search left
            if rate <= h:
                ans = min(ans, mid)
                r = mid - 1
            else:   
                l = mid + 1
                
        return ans