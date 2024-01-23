/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

func postorderRecursive(root *TreeNode, visited *[]int) {
    if root == nil {
        return
    }
    
    // visit left then right
    postorderRecursive(root.Left, visited)
    postorderRecursive(root.Right, visited)
    
    *visited = append(*visited, root.Val)

}
func postorderTraversal(root *TreeNode) []int {
    visited := []int{}
    postorderRecursive(root, &visited)
    return visited
}