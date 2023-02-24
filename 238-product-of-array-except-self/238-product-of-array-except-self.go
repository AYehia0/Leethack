
import "fmt"
func productExceptSelf(nums []int) []int {
    /*
    First, there is no way someone would get the O(n) solution if he haven't seen an optimal solution for it.
    The obvious answer is to use the division operation:
    
    prod = prod(input_list)
    nums[i] = prod/nums[i]
    
    
    The answer though is pretty simple, it's basically a math problem:
    Using a prefix, postfix arrays then multiply each res = prefix[i] * postfix[i]
    
    input:
    |a|b|c|d|
    
    prefix:
    |1|a|a * b|a * b * c|

    postfix:
    |b * c * d|c * d|d|1|
    
    res:
    |b * c * d| a * c * d|a * b * d|a * b * c|
    */
    
    res := make([]int, len(nums))
    
    // calculating the prefix (going forward)
    pre := 1
    for i, num := range nums {
        res[i] = pre
        pre *= num
    }
    
    // calculating the postfix (going backward)
    pos := 1
    for i := len(nums)-1;i>=0;i-- {
        res[i] *= pos
        pos *= nums[i]
    }
    
    return res
}