func merge(nums1 []int, m int, nums2 []int, n int)  {
    i := m - 1 // index for nums1 starts at m (end)
    j := n - 1 // index for nums2 starts at n (end)
    k := len(nums1) - 1 // index for the empty spaces in nums1 (end)
    
    for {
        if i < 0 || j < 0 {
            break
        }
        
        if nums1[i] <= nums2[j] {
            nums1[k] = nums2[j]
            j--
        }else {
            nums1[k] = nums1[i]
            i--
        }
        k--
    }
    
    // Copy any remaining elements from nums2 to nums1
    for j >= 0 {
        nums1[k] = nums2[j]
        j--
        k--
    }
}