func singleNonDuplicate(nums []int) int {
    // linear solution through XOR, since XOR of x with x = 0 we can use that to result the unique element : XOR (1, 1, 2) = 2
    ans := 0
    for _, num := range nums {
        ans ^= num
    }   
    return ans
}