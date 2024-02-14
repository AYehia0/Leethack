class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        t = 0
        for i in s:
            if i != " ":
                t += 1
            else:
                t = 0
        return t