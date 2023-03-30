class Solution:
    def mySqrt(self, x: int) -> int:
        # using the subtraction method (subtracting odd numbers)
        """
        square root of 16 using this method.

        16 - 1 = 15
        15 - 3 =12
        12 - 5 = 7
        7- 7 = 0

        You can observe that we have subtracted 4 times. Thus,√16 = 4
        
        """
        ans = 0
        odd = 1
        while x > 0:
            x -= odd
            odd += 2
            
            if x >= 0:
                ans += 1
        
        return ans
        