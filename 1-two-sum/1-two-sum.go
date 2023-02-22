import "fmt"

func twoSum(nums []int, target int) []int {
    ind1, ind2 := 0, 1
    if len(nums) == 2 {
        return []int{ind1, ind2}
    }
    // use a hashmap 
    h := make(map[int]int)
    for i, num := range nums {
        h[num] = i
    }
    for i, num := range nums {
        diff := target - num
        val, ok := h[diff]
        if ok && i != val {
            ind1 = i
            ind2 = val
            break
        }
    }
    return []int{ind1, ind2}
}