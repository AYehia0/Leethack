class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        h1, h2 = {}, {}
        # count the number of occurencies in both the 2 strings
        for i in range(len(s)):
            if s[i] not in h1:
                h1[s[i]] = 0
            else:
                h1[s[i]] += 1

            if t[i] not in h2:
                h2[t[i]] = 0
            else:
                h2[t[i]] += 1

        return True if h1==h2 else False

            