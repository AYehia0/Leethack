func removeDuplicates(nums []int) int {
    if len(nums) <= 2 {
        return len(nums)
    }
    
    l := 2
    
    for r := 2; r <= len(nums) - 1; r++ {
        if nums[l - 2] != nums[r] {
            nums[l] = nums[r]
            l++
        }
    }
    return l
}