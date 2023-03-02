class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = True
        r = len(s) - 1
        for ind, l in enumerate(s):
            if ind > r:
                break
            if not l.isalnum():
                continue
            while not s[r].isalnum():
                r -= 1
            if l.lower() != s[r].lower():
                palindrome = False
                break
            r -= 1
                
        return palindrome