func removeElement(nums []int, val int) int {
    k := len(nums)
    
    for i:=0; i<=len(nums)-1; i++ {
        if nums[i] == val {
            k--
            nums[i] = -1
        }
    }
    
    // sort
    sort.Sort(sort.Reverse(sort.IntSlice(nums)))
    
    return k
}