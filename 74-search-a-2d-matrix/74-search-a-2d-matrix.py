class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """The smart solution goes burrrrr, copied!!!"""
        rows = len(matrix)
        cols = len(matrix[0])
        currRow, currCol = 0, cols - 1
        
        while currRow < rows and currCol > -1:
            val = matrix[currRow][currCol]
            
            if target == val:
                return True
            
            # go down the tree
            if target > val:
                currRow += 1
            else:
                currCol -= 1
        return False