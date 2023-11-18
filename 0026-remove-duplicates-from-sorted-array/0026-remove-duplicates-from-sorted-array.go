func removeDuplicates(nums []int) int {
    l := 1

    for r := 1; r <= len(nums) - 1; r ++ {
        if nums[r] == nums[r-1] {
            continue
        }else {
            nums[l] = nums[r]
            l++
        }
    }
    return l
    
}