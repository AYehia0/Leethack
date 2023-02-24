func longestConsecutive(nums []int) int {
    /*
    Most obvious solution is sorting but it's O(nlogn)
    So there must be a better option, let's visualize the sets : [100,4,200,1,3,2]
    
    <-----1234-----------100---------200------>
         |- 4 -|         |1|         |1|
    how can we mark/group sets ?
    by telling the beginning of the set, in this example the beginning of a set, is a number which doesn't have any neighbours (requires a hashmap) : 1 is the start of a group/set as it doesn't have smaller value 0.
    
    */
    
    m := make(map[int]bool)
    
    for _, num := range nums {
        if _, ok := m[num]; !ok {
            m[num] = true
        }
    }
    
    longest := 0
    for _, num := range nums {
        // check the beginning of set
        if _, ok := m[num-1]; !ok {
            co := 0
            // while the num has consecutives : if it exists in the set 1 + 1 --> 1 + 2 ...
            for m[num + co] {
                co++
            }
            if co > longest {
                longest = co
            }
        }
    }

    return longest
}