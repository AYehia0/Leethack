// using the xor (bitwise)
func singleNumber(nums []int) int {
    ans := 0
    
    for _,k := range nums {
        ans ^= k
    }
    return ans
}