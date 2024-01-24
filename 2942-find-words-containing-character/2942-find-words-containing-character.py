class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for ind, w in enumerate(words):
            if x in w:
                ans += [ind]
                
        return ans