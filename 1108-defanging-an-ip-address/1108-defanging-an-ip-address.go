func defangIPaddr(address string) string {
    ans := ""
    
    for _,s := range address {
        if string(s) != "." {
            ans += string(s)
        }else {
            ans += "[.]"
        }
    }
    return ans
}