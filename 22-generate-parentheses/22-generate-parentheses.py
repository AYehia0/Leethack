class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        n = 3, so all the posssible solutions are 3! = 6 but we can't start with opened one!
        """
        ans = []
        opened = closed = 0
        
        
        # doing backtracking recursivly
        # we can only add closing pren if only the opened > closed : ( ( )
        # we can't exceed the limit of added opened prens (if we already have n=3 "((())", we don't have a choice but closed ones)
        def bkt(opened, closed, stack):
            if opened == closed == n:
                ans.append("".join(stack))
                return
            
            # add closing one
            if opened > closed:
                bkt(opened, closed+1, stack + [")"])
            
            if opened < n:
                bkt(opened + 1, closed, stack + ["("])
            
        bkt(opened, closed, [])
        return ans