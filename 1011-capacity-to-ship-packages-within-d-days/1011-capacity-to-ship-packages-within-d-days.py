class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        m = sum(weights)
        
        def checkWeight(weights, days, d):
            x = 1
            curr_sum = 0
            for i in range(len(weights)):
                curr_sum += weights[i]
                if curr_sum > d:
                    curr_sum = weights[i]
                    x += 1

            return x <= days
        
        # O(n * m) timeouts 
        # for i in range(max(max(weights), 1), m+1):
        #     if checkWeight(weights, days, i):
        #         return i
        
        l, r = max(weights), m
        while l < r:
            mid = l + (r - l)//2
            
            if checkWeight(weights, days, mid):
                r = mid
            else:
                l = mid + 1
        return l