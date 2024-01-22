func isPerfectSquare(num int) bool {
    l, r := 0, num
    
    for {
        m := l + (r - l)/2
        
        if l > r {
            break
        }
        
        if m*m > num {
            r = m - 1
        }else if m*m < num {
            l = m + 1
        }else {
            return true
        }
    }
    return false
}