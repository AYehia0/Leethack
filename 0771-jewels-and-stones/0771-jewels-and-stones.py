class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        s = Counter(stones)
        for j in jewels:
            ans += s.get(j, 0)
        return ans
                
            
        