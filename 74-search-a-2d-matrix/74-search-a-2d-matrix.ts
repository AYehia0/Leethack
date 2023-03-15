function searchMatrix(matrix: number[][], target: number): boolean {
    /*
    There are multiple approaches to solve this problem, 
        - The easiest is to do m binary searches for each row in the list.
        - Another one is to do 2 binary searches, one to find the row, as "The first integer of each row is greater than the last integer of the previous row." therfore we can find which row to search for example take 3 as target, first value of the second row 10, last is 20 so it can't be inbetween or down, must be above. The second binary search is to find the target in row.
        - One smart approach that I found on leetcode discussions : https://leetcode.com/problems/search-a-2d-matrix/discuss/1895837 is to deal with the 2d array as tree (binary search tree)
    */
    
    // finding the row
    let top : number = 0
    let bottom : number = matrix.length - 1
    while (top <= bottom) {
        let row : number = Math.floor((top + bottom) / 2)
        if (target < matrix[row][0]) {
            bottom = row - 1
        }else if (target > matrix[row].at(-1)) {
            top = row + 1
        }else break
    }
    
    if (!(top <= bottom)) return false
    
    // finding the target in that row
    let row : number = Math.floor((top + bottom) / 2)
    let left : number = 0
    let right : number = matrix[0].length - 1
    while (left <= right) {
        let mid = Math.floor((left + right) / 2)
        if (target < matrix[row][mid]) {
            right = mid - 1
        }else if (target > matrix[row][mid]) {
            left = mid + 1
        }else return true
    }
    return false
};