func isValid(s string) bool {
    prens := map[string]string{
        ")": "(",
        "]": "[",
        "}": "{",
    }
    st := []string{}
    for _, ch := range s {
        if val, ok := prens[string(ch)]; ok && len(st) > 0 && st[len(st)-1] == val {
            st = st[:len(st)-1]
        } else {
            st = append(st, string(ch))
        }
    }
    return len(st) == 0
}
