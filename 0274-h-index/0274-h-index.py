class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations, reverse=True)
        
        # [6, 5, 3, 1, 0]
        # [0, 1, 2, 3, 4]
        for i in range(len(citations)):
            if i >= citations[i]:
                return i
        return len(citations)
