func mySqrt(x int) int {
    // while we can use odd subtraction of each iteration : 
    // sqrt(16) = 4
    // 16 - 1 = 15
    // 15 - 3 = 12
    // 12 - 5 = 7
    // 7 - 7 = 0
    // answer is the number of subs till subtraction is less than or equal to 0
    
    // another way to solve this using binary search
    
    l, r := 0, x
    ans := 0
    for {
        m := l + (r - l)/2
        
        if l > r {
            break
        }
        
        if m*m > x {
            r = m - 1
        }else if m*m < x {
            l = m + 1
            ans = m
        }else {
            return m
        }
    }
    
    return ans
}