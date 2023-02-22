func containsDuplicate(nums []int) bool {
    h := make(map[int]int)
    for _, num := range nums {
        _, ok := h[num]
        if !ok {
            h[num] = 1
        }else {
            h[num]++
        }
    }

    for _, v := range h {
        if v > 1 {
            return true
        }
    }
    return false
}