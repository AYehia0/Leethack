class Solution:
    def secondHighest(self, s: str) -> int:
        m = []
        for i in s:
            if i.isdigit() and i not in m:
                m.append(i)
                
        m.sort(reverse=True)
        return int(m[1]) if len(m) > 1 else -1
                