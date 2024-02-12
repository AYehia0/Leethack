class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # edge cases
        if len(t) > len(s):
            return ""
        
        if len(t) == len(s) and s == t:
            return s
        
        # need: the chars we need to find
        need_map = {}
        for i, c in enumerate(t):
            if c not in need_map:
                need_map[c] = 1
            else:
                need_map[c] += 1
        
        need_num = len(need_map)
        
        # haves
        have_num = 0
        window = {}
        
        min_len = math.inf
        min_range = (-1, -1)
        
        l = 0
        
        for r in range(len(s)):
            tmp = s[r]
            
            if tmp not in window:
                window[tmp] = 1
            else:
                window[tmp] += 1
                
            # check if we have that
            if tmp in need_map and need_map[tmp] == window[tmp]:
                have_num += 1
                
            # now do that for all the char while poping left
            while have_num == need_num:
                
                # update the result
                mm = (r - l + 1)
                if mm < min_len:
                    min_len = mm
                    min_range = (l, r)
                
                # pop from the left and check if the condition is meet too 
                window[s[l]] -= 1
                if s[l] in need_map and window[s[l]] < need_map[s[l]]:
                    have_num -= 1
                    
                l += 1
        
        x, y = min_range
        return s[x:y+1]
        