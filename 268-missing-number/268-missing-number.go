func missingNumber(nums []int) int {
    n := len(nums)
    sum := (n * (n + 1)) / 2
    
    for _,i := range nums {
        sum -= i
    }
    return sum
}