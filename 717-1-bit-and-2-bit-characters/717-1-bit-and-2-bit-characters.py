class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        ns, i = len(bits), 0
        ans = False
        while i < ns:
            if bits[i] == 1:
                i += 2
                ans = False
            else:
                i += 1
                ans = True
        return ans