class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ans = []
        l1 = s1.split(" ")
        l2 = s2.split(" ")
        
        # a word is uncommon if exists in one sentence (once) AND doesn't exist in the other
        # check existence in the first sentence
        for w1 in l1:
            if l1.count(w1) > 1:
                continue
            if w1 not in set(l2):
                ans.append(w1)
                
        for w2 in l2:
            if l2.count(w2) > 1:
                continue
            if w2 not in set(l1):
                ans.append(w2)
        
        return ans
        
        