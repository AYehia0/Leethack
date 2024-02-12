class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # it's unique coz the set must be unique
        window = set()
        ans = 0
        l = 0
        for r in range(len(s)):
            t = s[r]
            
            while t in window:
                # update the window, remove from left
                window.remove(s[l])
                
                # update the left pointer
                l += 1
            
            # add to the set
            window.add(t)
            
            # calculating the longest
            mm = (r - l + 1)
            
            # update the answer
            ans = max(ans, mm)
            
        return ans