class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        A Gap between heights ? 
        
            - heights = [2, 1, 1]          ---> Area 1 * 3 = 3
            - heights = [4, 4, 7, 1]       ---> Area 3 * 4 = 12
            - heights = [4, 4, 1, 7, 1]    ---> Area 2 * 4 = 8
            
        This problem is so similar to the previous one : 853 car fleet
        """
        
        max_area = 0
        st = [] # pairs of (index, height)
        for i, h in enumerate(heights):
            start_ind = i
            # increasing of heights
            while st and st[-1][1] > h:
                index, height = st.pop()
                
                # calculate the max area so far
                max_area = max(max_area, (i - index) * height)
                
                start_ind = index
            st.append((start_ind, h))
        
        # calculate the rest of height of one height till the end of the widths
        for i, h in st:
            max_area = max(max_area, h * (len(heights) - i))
        
        return max_area