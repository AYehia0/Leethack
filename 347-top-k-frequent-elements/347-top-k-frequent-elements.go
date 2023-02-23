func topKFrequent(nums []int, k int) []int {
    h := make(map[int]int)
    bucket := make([][]int, len(nums) + 1)
    ans := make([]int, 0)
    
    if len(nums) == k {
        return nums
    }
    
    for _, num := range nums {
        if _, ok := h[num]; !ok {
            h[num] = 1
        }else {
            h[num]++
        }
    }

    for key, val := range h {
        bucket[val] = append(bucket[val], key)
    }

    for i := len(bucket)-1; i >= 0; i-- {
        ans = append(ans, bucket[i]...)
        if len(ans) == k {
            break
        }
    }
    return ans
}